"""Automated Data-Driven Unit Test Suite (Task 3).

Author: M. Ahmad Naeem (Roll No: 23F-3113)
Technique: Data-Driven Testing consuming external CSV test dataset
Target Functions:
    - validators.between
    - validators.length
    - validators.email
Dataset: data/test_data_ahmad.csv
"""

import csv
from pathlib import Path
import pytest
import validators
from validators import ValidationError


DATA_FILE = Path(__file__).parent.parent / "data" / "test_data_ahmad.csv"


def load_csv_test_data():
    """Load test cases from the external CSV file."""
    test_cases = []
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_cases.append(row)
    return test_cases


ALL_CASES = load_csv_test_data()


@pytest.mark.ahmad_suite
@pytest.mark.data_driven
@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[case["test_id"] for case in ALL_CASES],
)
def test_data_driven_from_csv(case):
    """Execute automated unit test case consuming data from external CSV file."""
    func_name = case["function_name"]
    raw_input = case["input_val"]
    expected_bool = case["expected"].strip().lower() == "true"

    if func_name == "between":
        val = int(raw_input)
        min_v = int(case["min_val"]) if case["min_val"] else None
        max_v = int(case["max_val"]) if case["max_val"] else None
        result = validators.between(val, min_val=min_v, max_val=max_v)

    elif func_name == "length":
        val = str(raw_input)
        min_v = int(case["min_val"]) if case["min_val"] else None
        max_v = int(case["max_val"]) if case["max_val"] else None
        result = validators.length(val, min_val=min_v, max_val=max_v)

    elif func_name == "email":
        val = str(raw_input)
        result = validators.email(val)

    else:
        pytest.fail(f"Unknown function in CSV test data: {func_name}")

    if expected_bool:
        assert result is True, (
            f"Failed on {case['test_id']}: Expected True but got {result} for input {raw_input}"
        )
    else:
        assert isinstance(result, ValidationError), (
            f"Failed on {case['test_id']}: Expected ValidationError but got {result} for input {raw_input}"
        )
        assert bool(result) is False
