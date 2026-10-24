"""Automated Unit Test Suite for Module 1: Range & Length Validation.

Author: M. Ahmad Naeem (Roll No: 23F-3113)
Techniques Applied: Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA)
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

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_between_ecp_valid_middle_nominal(self):
        """ECP-BET-01: Valid nominal value strictly inside boundaries."""
        result = validators.between(15, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_between_bva_lower_boundary_min(self):
        """BVA-BET-01: Value exactly at lower boundary (min_val)."""
        result = validators.between(10, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_between_bva_upper_boundary_max(self):
        """BVA-BET-02: Value exactly at upper boundary (max_val)."""
        result = validators.between(20, min_val=10, max_val=20)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_between_bva_just_below_min_invalid(self):
        """BVA-BET-03: Value just below lower boundary (min - 1)."""
        result = validators.between(9, min_val=10, max_val=20)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_between_bva_just_above_max_invalid(self):
        """BVA-BET-04: Value just above upper boundary (max + 1)."""
        result = validators.between(21, min_val=10, max_val=20)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_between_ecp_only_min_val_provided(self):
        """ECP-BET-04: Open range with only min_val specified."""
        assert validators.between(100, min_val=50) is True
        assert isinstance(validators.between(49, min_val=50), ValidationError)

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_between_ecp_only_max_val_provided(self):
        """ECP-BET-05: Open range with only max_val specified."""
        assert validators.between(25, max_val=50) is True
        assert isinstance(validators.between(51, max_val=50), ValidationError)

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_between_ecp_float_boundaries(self):
        """ECP-BET-07: Floating point numbers within boundaries."""
        assert validators.between(13.5, min_val=10.2, max_val=15.8) is True
        assert isinstance(validators.between(10.19, min_val=10.2, max_val=15.8), ValidationError)

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_between_ecp_datetime_range(self):
        """ECP-BET-08: Comparable datetime objects."""
        target_date = datetime(2026, 6, 15)
        min_date = datetime(2026, 1, 1)
        max_date = datetime(2026, 12, 31)
        assert validators.between(target_date, min_val=min_date, max_val=max_date) is True

    @pytest.mark.ahmad_suite
    @pytest.mark.exception
    def test_between_exception_inverted_bounds(self):
        """ECP-BET-12: Inverted bounds (min_val > max_val) returns ValidationError with reason."""
        result = validators.between(15, min_val=30, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "`min_val` cannot be greater than `max_val`" in str(result.args)


# ============================================================================
# FUNCTION 2: validators.length(value, min_val, max_val)
# ============================================================================

class TestLengthAhmad:
    """Test suite covering validators.length using ECP and BVA."""

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_length_ecp_valid_nominal_length(self):
        """ECP-LEN-01: String length strictly inside range [5, 10]."""
        result = validators.length("abcdef", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_exact_min_length(self):
        """BVA-LEN-01: String length exactly at lower boundary (len=5)."""
        result = validators.length("hello", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_exact_max_length(self):
        """BVA-LEN-02: String length exactly at upper boundary (len=10)."""
        result = validators.length("1234567890", min_val=5, max_val=10)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_just_below_min_length_invalid(self):
        """BVA-LEN-03: String length just below lower bound (len=4)."""
        result = validators.length("four", min_val=5, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_just_above_max_length_invalid(self):
        """BVA-LEN-04: String length just above upper bound (len=11)."""
        result = validators.length("eleven11111", min_val=5, max_val=10)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.ahmad_suite
    @pytest.mark.ecp
    def test_length_ecp_exact_length_match(self):
        """ECP-LEN-04: Strict exact length requirement (min_val == max_val)."""
        assert validators.length("pin1", min_val=4, max_val=4) is True
        assert isinstance(validators.length("pin12", min_val=4, max_val=4), ValidationError)

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_empty_string_with_zero_min(self):
        """ECP-LEN-07: Empty string (len=0) with min_val=0."""
        result = validators.length("", min_val=0, max_val=5)
        assert result is True

    @pytest.mark.ahmad_suite
    @pytest.mark.bva
    def test_length_bva_empty_string_with_positive_min_invalid(self):
        """BVA-LEN-05: Empty string (len=0) when min_val=1."""
        result = validators.length("", min_val=1, max_val=5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.ahmad_suite
    @pytest.mark.exception
    def test_length_exception_negative_min_val(self):
        """ECP-LEN-11: Negative min_val returns ValidationError with reason."""
        result = validators.length("test", min_val=-1, max_val=5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "Length cannot be negative" in str(result.args)

    @pytest.mark.ahmad_suite
    @pytest.mark.exception
    def test_length_exception_negative_max_val(self):
        """ECP-LEN-12: Negative max_val returns ValidationError with reason."""
        result = validators.length("test", min_val=1, max_val=-5)
        assert isinstance(result, ValidationError)
        assert bool(result) is False
        assert "Length cannot be negative" in str(result.args)
