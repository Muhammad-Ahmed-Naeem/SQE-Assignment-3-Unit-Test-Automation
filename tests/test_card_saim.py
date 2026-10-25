# Tests for Module 3: credit card and visa validation
# Saim Naveed (24F-3043)

import pytest
import validators
from validators import ValidationError


@pytest.mark.order(58)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.smoke
@pytest.mark.ecp
def test_card_valid_luhn():
    # standard 16 digit card number passing Luhn algorithm
    assert validators.card_number("4242424242424242") is True


@pytest.mark.order(59)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.ecp
def test_card_invalid_luhn_checksum():
    # last digit altered so checksum check fails
    res = validators.card_number("4242424242424241")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(60)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.ecp
def test_card_non_numeric_input():
    # alphabetic characters in card number
    res = validators.card_number("4242abcd42424242")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(61)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.ecp
def test_card_empty_string():
    res = validators.card_number("")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(62)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.smoke
@pytest.mark.ecp
def test_visa_valid_standard_16_digits():
    # valid 16 digit Visa card (starts with 4)
    assert validators.visa("4242424242424242") is True


@pytest.mark.order(63)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.bva
def test_card_13_digit_valid():
    # 13 digit card passing Luhn
    assert validators.card_number("4012888888881") is True


@pytest.mark.order(64)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.bva
def test_visa_length_boundary_must_be_16():
    # visa validator strictly checks for 16 digits
    res = validators.visa("4012888888881")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(65)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.ecp
def test_visa_rejects_mastercard():
    # Mastercard starts with 5, must be rejected by visa()
    res = validators.visa("5105105105105100")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(66)
@pytest.mark.saim_suite
@pytest.mark.card_suite
@pytest.mark.ecp
@pytest.mark.parametrize(
    "card_val,expected_valid",
    [
        ("4111111111111111", True),
        ("4012888888881881", True),
        ("1234567890123456", False),
        ("0000000000000000", True),
        ("4", False),
        ("4242-4242-4242-4242", False),
    ],
    ids=["visa_alt", "valid_luhn_alt", "bad_checksum", "all_zeros_luhn", "single_digit", "with_hyphens"]
)
def test_card_parameterized(card_val, expected_valid):
    res = validators.card_number(card_val)
    if expected_valid:
        assert res is True
    else:
        assert isinstance(res, ValidationError)
        assert bool(res) is False
