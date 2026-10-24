# Data-driven tests reading from external CSV
# M. Ahmad Naeem (23F-3113)

import csv
from pathlib import Path
import pytest
import validators
from validators import ValidationError

DATA_FILE = Path(__file__).parent.parent / "data" / "test_data_ahmad.csv"


def load_cases():
    cases = []
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cases.append(row)
    return cases


TEST_CASES = load_cases()


@pytest.mark.ahmad_suite
@pytest.mark.data_driven
@pytest.mark.parametrize(
    "case",
    TEST_CASES,
    ids=[c["test_id"] for c in TEST_CASES],
)
def test_csv_driven(case):
    func_name = case["function_name"]
    raw_input = case["input_val"]
    expected = case["expected"].strip().lower() == "true"

    if func_name == "between":
        v = int(raw_input)
        min_v = int(case["min_val"]) if case["min_val"] else None
        max_v = int(case["max_val"]) if case["max_val"] else None
        res = validators.between(v, min_val=min_v, max_val=max_v)

    elif func_name == "length":
        v = str(raw_input)
        min_v = int(case["min_val"]) if case["min_val"] else None
        max_v = int(case["max_val"]) if case["max_val"] else None
        res = validators.length(v, min_val=min_v, max_val=max_v)

    elif func_name == "email":
        v = str(raw_input)
        res = validators.email(v)

    else:
        pytest.fail(f"Unexpected function: {func_name}")

    if expected:
        assert res is True
    else:
        assert isinstance(res, ValidationError)
        assert bool(res) is False
