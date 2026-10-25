# Data-driven tests for Saim's modules
# Saim Naveed (24F-3043)

import csv
from pathlib import Path
import pytest
import validators
from validators import ValidationError

DATA_FILE = Path(__file__).parent.parent / "data" / "test_data_saim.csv"


def get_test_rows():
    rows = []
    with open(DATA_FILE, mode="r", encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        for r in reader:
            rows.append(r)
    return rows


SAIM_TEST_DATA = get_test_rows()


@pytest.mark.saim_suite
@pytest.mark.data_driven
@pytest.mark.parametrize(
    "item",
    SAIM_TEST_DATA,
    ids=[x["test_id"] for x in SAIM_TEST_DATA],
)
def test_saim_csv_cases(item):
    fn = item["function_name"]
    val = item["input_val"]
    should_pass = item["expected"].strip().lower() == "true"

    if fn == "domain":
        res = validators.domain(val)
    elif fn == "ipv4":
        res = validators.ipv4(val)
    elif fn == "card":
        res = validators.card_number(val)
    else:
        pytest.fail(f"Unknown target function: {fn}")

    if should_pass:
        assert res is True
    else:
        assert isinstance(res, ValidationError)
        assert bool(res) is False
