"""Automated Unit Test Suite for Module 1: Range & Length Validation.

Author: M. Ahmad Naeem (Roll No: 23F-3113)
Techniques Applied: Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA)
Task 4 Features: Test suites/markers, test parameterization, execution ordering
Target Functions:
    - validators.between (between.py)
    - validators.length (length.py)
"""

from datetime import datetime
import pytest
import validators
from validators import ValidationError


# ============================================================================
# FUNCTION 1: validators.between(value, min_val, max_val)
# ============================================================================

class TestBetweenAhmad:
    """Test suite covering validators.between using ECP and BVA."""

    @pytest.mark.order(1)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_between_ecp_valid_middle_nominal(self):
        """ECP-BET-01: Valid nominal value strictly inside boundaries."""
        result = validators.between(15, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.order(2)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_bva_lower_boundary_min(self):
        """BVA-BET-01: Value exactly at lower boundary (min_val)."""
        result = validators.between(10, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.order(3)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_bva_upper_boundary_max(self):
        """BVA-BET-02: Value exactly at upper boundary (max_val)."""
        result = validators.between(20, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.order(4)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_bva_just_below_min_invalid(self):
        """BVA-BET-03: Value just below lower boundary (min - 1)."""
        result = validators.between(9, min_val=10, max_val=20)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(5)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_between_bva_just_above_max_invalid(self):
        """BVA-BET-04: Value just above upper boundary (max + 1)."""
        result = validators.between(21, min_val=10, max_val=20)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(6)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_ecp_only_min_val_provided(self):
        """ECP-BET-04: Open range with only min_val specified."""
        assert validators.between(100, min_val=50) is True
        assert isinstance(validators.between(49, min_val=50), ValidationError)

    @pytest.mark.order(7)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_ecp_only_max_val_provided(self):
        """ECP-BET-05: Open range with only max_val specified."""
        assert validators.between(25, max_val=50) is True
        assert isinstance(validators.between(51, max_val=50), ValidationError)

    @pytest.mark.order(8)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_ecp_float_boundaries(self):
        """ECP-BET-07: Floating point numbers within boundaries."""
        assert validators.between(13.5, min_val=10.2, max_val=15.8) is True
        assert isinstance(validators.between(10.19, min_val=10.2, max_val=15.8), ValidationError)

    @pytest.mark.order(9)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_between_ecp_datetime_range(self):
        """ECP-BET-08: Comparable datetime objects."""
        target_date = datetime(2026, 6, 15)
        min_date = datetime(2026, 1, 1)
        max_date = datetime(2026, 12, 31)
        assert validators.between(target_date, min_val=min_date, max_val=max_date) is True

    @pytest.mark.order(10)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_between_exception_inverted_bounds(self):
        """ECP-BET-12: Inverted bounds (min_val > max_val) returns ValidationError with reason."""
        result = validators.between(15, min_val=30, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "`min_val` cannot be greater than `max_val`" in str(result.args)

    # ------------------------------------------------------------------------
    # Task 4: Parameterized Data-Driven Test Suite for between boundaries
    # ------------------------------------------------------------------------
    @pytest.mark.order(11)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    @pytest.mark.parametrize(
        "val,min_val,max_val,expected_valid",
        [
            (9, 10, 20, False),    # Min - 1
            (10, 10, 20, True),    # Min
            (11, 10, 20, True),    # Min + 1
            (15, 10, 20, True),    # Nominal
            (19, 10, 20, True),    # Max - 1
            (20, 10, 20, True),    # Max
            (21, 10, 20, False),   # Max + 1
        ],
        ids=["min_minus_1", "min_boundary", "min_plus_1", "nominal", "max_minus_1", "max_boundary", "max_plus_1"]
    )
    def test_between_parameterized_bva(self, val, min_val, max_val, expected_valid):
        """Task 4: Parameterized data-driven test evaluating all BVA boundary points."""
        res = validators.between(val, min_val=min_val, max_val=max_val)
        if expected_valid:
            assert res is True
        else:
            assert isinstance(res, ValidationError)
            assert bool(res) is False


# ============================================================================
# FUNCTION 2: validators.length(value, min_val, max_val)
# ============================================================================

class TestLengthAhmad:
    """Test suite covering validators.length using ECP and BVA."""

    @pytest.mark.order(12)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_length_ecp_valid_nominal_length(self):
        """ECP-LEN-01: String length strictly inside range [5, 10]."""
        result = validators.length("abcdef", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.order(13)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_exact_min_length(self):
        """BVA-LEN-01: String length exactly at lower boundary (len=5)."""
        result = validators.length("hello", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.order(14)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_exact_max_length(self):
        """BVA-LEN-02: String length exactly at upper boundary (len=10)."""
        result = validators.length("1234567890", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.order(15)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_just_below_min_length_invalid(self):
        """BVA-LEN-03: String length just below lower bound (len=4)."""
        result = validators.length("four", min_val=5, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(16)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_just_above_max_length_invalid(self):
        """BVA-LEN-04: String length just above upper bound (len=11)."""
        result = validators.length("eleven11111", min_val=5, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(17)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.ecp
    def test_length_ecp_exact_length_match(self):
        """ECP-LEN-04: Strict exact length requirement (min_val == max_val)."""
        assert validators.length("pin1", min_val=4, max_val=4) is True
        assert isinstance(validators.length("pin12", min_val=4, max_val=4), ValidationError)

    @pytest.mark.order(18)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_empty_string_with_zero_min(self):
        """ECP-LEN-07: Empty string (len=0) with min_val=0."""
        result = validators.length("", min_val=0, max_val=5)
        assert result is True

    @pytest.mark.order(19)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    def test_length_bva_empty_string_with_positive_min_invalid(self):
        """BVA-LEN-05: Empty string (len=0) when min_val=1."""
        result = validators.length("", min_val=1, max_val=5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(20)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_length_exception_negative_min_val(self):
        """ECP-LEN-11: Negative min_val returns ValidationError with reason."""
        result = validators.length("test", min_val=-1, max_val=5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "Length cannot be negative" in str(result.args)

    @pytest.mark.order(21)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.exception
    def test_length_exception_negative_max_val(self):
        """ECP-LEN-12: Negative max_val returns ValidationError with reason."""
        result = validators.length("test", min_val=1, max_val=-5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "Length cannot be negative" in str(result.args)

    # ------------------------------------------------------------------------
    # Task 4: Parameterized Data-Driven Test Suite for length boundaries
    # ------------------------------------------------------------------------
    @pytest.mark.order(22)
    @pytest.mark.ahmad_suite
    @pytest.mark.range_suite
    @pytest.mark.bva
    @pytest.mark.parametrize(
        "string_val,min_val,max_val,expected_valid",
        [
            ("four", 5, 10, False),        # Len 4 (Min - 1)
            ("five5", 5, 10, True),        # Len 5 (Min)
            ("six666", 5, 10, True),       # Len 6 (Min + 1)
            ("ten1010100", 5, 10, True),   # Len 10 (Max)
            ("eleven11111", 5, 10, False), # Len 11 (Max + 1)
        ],
        ids=["len_4_invalid", "len_5_valid", "len_6_valid", "len_10_valid", "len_11_invalid"]
    )
    def test_length_parameterized_bva(self, string_val, min_val, max_val, expected_valid):
        """Task 4: Parameterized data-driven test evaluating string length boundaries."""
        res = validators.length(string_val, min_val=min_val, max_val=max_val)
        if expected_valid:
            assert res is True
        else:
            assert isinstance(res, ValidationError)
            assert bool(res) is False
