# Tests for Module 1: between and length validation
# M. Ahmad Naeem (23F-3113)

from datetime import datetime
import pytest
import validators
from validators import ValidationError


class TestBetweenAhmad:

    @pytest.mark.order(1)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_between_nominal(self):
        # Valid middle value in closed range [10, 20]
        assert validators.between(15, min_val=10, max_val=20) is True

    @pytest.mark.order(2)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_min_boundary(self):
        # Exact lower boundary value
        assert validators.between(10, min_val=10, max_val=20) is True

    @pytest.mark.order(3)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_max_boundary(self):
        # Exact upper boundary value
        assert validators.between(20, min_val=10, max_val=20) is True

    @pytest.mark.order(4)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_below_min(self):
        # One below min boundary
        res = validators.between(9, min_val=10, max_val=20)
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(5)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_above_max(self):
        # One above max boundary
        res = validators.between(21, min_val=10, max_val=20)
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(6)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_only_min(self):
        # Unbounded upper limit
        assert validators.between(100, min_val=50) is True
        assert isinstance(validators.between(49, min_val=50), ValidationError)

    @pytest.mark.order(7)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_only_max(self):
        # Unbounded lower limit
        assert validators.between(25, max_val=50) is True
        assert isinstance(validators.between(51, max_val=50), ValidationError)

    @pytest.mark.order(8)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_floats(self):
        # Floating point values
        assert validators.between(13.5, min_val=10.2, max_val=15.8) is True
        assert isinstance(validators.between(10.19, min_val=10.2, max_val=15.8), ValidationError)

    @pytest.mark.order(9)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_dates(self):
        # Datetime comparison
        target = datetime(2026, 6, 15)
        d_min = datetime(2026, 1, 1)
        d_max = datetime(2026, 12, 31)
        assert validators.between(target, min_val=d_min, max_val=d_max) is True

    @pytest.mark.order(10)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_between_invalid_bounds(self):
        # min_val greater than max_val should fail validation
        res = validators.between(15, min_val=30, max_val=10)
        assert isinstance(res, ValidationError)
        assert "`min_val` cannot be greater than `max_val`" in str(res.args)

    @pytest.mark.order(11)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    @pytest.mark.parametrize(
        "val,min_val,max_val,expected_valid",
        [
            (9, 10, 20, False),
            (10, 10, 20, True),
            (11, 10, 20, True),
            (15, 10, 20, True),
            (19, 10, 20, True),
            (20, 10, 20, True),
            (21, 10, 20, False),
        ],
        ids=["min_minus_1", "min_exact", "min_plus_1", "nominal", "max_minus_1", "max_exact", "max_plus_1"]
    )
    def test_between_boundary_dataset(self, val, min_val, max_val, expected_valid):
        res = validators.between(val, min_val=min_val, max_val=max_val)
        if expected_valid:
            assert res is True
        else:
            assert isinstance(res, ValidationError)
            assert bool(res) is False


class TestLengthAhmad:

    @pytest.mark.order(12)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_length_nominal(self):
        # String length within [5, 10]
        assert validators.length("abcdef", min_val=5, max_val=10) is True

    @pytest.mark.order(13)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_min_boundary(self):
        # Exactly 5 characters
        assert validators.length("hello", min_val=5, max_val=10) is True

    @pytest.mark.order(14)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_max_boundary(self):
        # Exactly 10 characters
        assert validators.length("1234567890", min_val=5, max_val=10) is True

    @pytest.mark.order(15)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_below_min(self):
        # 4 characters when min is 5
        res = validators.length("four", min_val=5, max_val=10)
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(16)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_above_max(self):
        # 11 characters when max is 10
        res = validators.length("eleven11111", min_val=5, max_val=10)
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(17)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_length_exact_pin(self):
        # Exact length match
        assert validators.length("pin1", min_val=4, max_val=4) is True
        assert isinstance(validators.length("pin12", min_val=4, max_val=4), ValidationError)

    @pytest.mark.order(18)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_empty_string_allowed(self):
        # Empty string with min_val 0
        assert validators.length("", min_val=0, max_val=5) is True

    @pytest.mark.order(19)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_empty_string_rejected(self):
        # Empty string when min_val is positive
        res = validators.length("", min_val=1, max_val=5)
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(20)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_length_negative_min(self):
        # Negative bounds are invalid
        res = validators.length("test", min_val=-1, max_val=5)
        assert isinstance(res, ValidationError)
        assert "Length cannot be negative" in str(res.args)

    @pytest.mark.order(21)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_length_negative_max(self):
        # Negative bounds are invalid
        res = validators.length("test", min_val=1, max_val=-5)
        assert isinstance(res, ValidationError)
        assert "Length cannot be negative" in str(res.args)

    @pytest.mark.order(22)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    @pytest.mark.parametrize(
        "string_val,min_val,max_val,expected_valid",
        [
            ("four", 5, 10, False),
            ("five5", 5, 10, True),
            ("six666", 5, 10, True),
            ("ten1010100", 5, 10, True),
            ("eleven11111", 5, 10, False),
        ],
        ids=["len_4_invalid", "len_5_valid", "len_6_valid", "len_10_valid", "len_11_invalid"]
    )
    def test_length_boundary_dataset(self, string_val, min_val, max_val, expected_valid):
        res = validators.length(string_val, min_val=min_val, max_val=max_val)
        if expected_valid:
            assert res is True
        else:
            assert isinstance(res, ValidationError)
            assert bool(res) is False
