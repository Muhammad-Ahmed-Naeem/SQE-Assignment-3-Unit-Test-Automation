"""Automated Unit Test Suite for Module 2: Contact Validation (Email).

Author: M. Ahmad Naeem (Roll No: 23F-3113)
Techniques Applied: Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA)
Task 4 Features: Test suites/markers, test parameterization, execution ordering
Target Function:
    - validators.email (email.py)
"""

import pytest
import validators
from validators import ValidationError


class TestEmailAhmad:
    """Test suite covering validators.email using ECP and BVA."""

    @pytest.mark.order(23)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_email_ecp_standard_valid(self):
        """ECP-EML-01: Standard valid email address."""
        result = validators.email("test.user@example.com")
        assert result is True

    @pytest.mark.order(24)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_subdomain_valid(self):
        """ECP-EML-02: Valid email with multi-level subdomain."""
        result = validators.email("ahmad.naeem@student.fast.edu.pk")
        assert result is True

    @pytest.mark.order(25)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_special_characters_in_username(self):
        """ECP-EML-03: Valid email containing allowable characters (+, ., _, -)."""
        result = validators.email("ahmad+sqe_test@example-domain.org")
        assert result is True

    @pytest.mark.order(26)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_numeric_username_and_domain(self):
        """ECP-EML-04: Valid email with numeric username and domain."""
        result = validators.email("233113@domain123.com")
        assert result is True

    @pytest.mark.order(27)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_missing_at_symbol_invalid(self):
        """ECP-EML-06: Invalid email missing @ symbol."""
        result = validators.email("ahmadnaeemexample.com")
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(28)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_multiple_at_symbols_invalid(self):
        """ECP-EML-07: Invalid email containing multiple @ symbols."""
        result = validators.email("ahmad@@example.com")
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(29)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_missing_local_username_invalid(self):
        """ECP-EML-08: Invalid email with empty username/local part."""
        result = validators.email("@example.com")
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(30)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_missing_domain_invalid(self):
        """ECP-EML-09: Invalid email with empty domain part."""
        result = validators.email("ahmad@")
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(31)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_bva_username_max_boundary_64_chars(self):
        """BVA-EML-01: Username exactly at RFC 5321 max boundary (64 chars)."""
        username_64 = "a" * 64
        email_input = f"{username_64}@example.com"
        result = validators.email(email_input)
        assert result is True

    @pytest.mark.order(32)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_bva_username_exceeds_max_boundary_65_chars(self):
        """BVA-EML-02: Username exceeding RFC 5321 limit by 1 char (65 chars)."""
        username_65 = "a" * 65
        email_input = f"{username_65}@example.com"
        result = validators.email(email_input)
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    @pytest.mark.order(33)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_bva_single_char_username_min_boundary(self):
        """BVA-EML-03: Single character username minimum boundary (len=1)."""
        result = validators.email("a@example.com")
        assert result is True

    @pytest.mark.order(34)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_ecp_invalid_space_character(self):
        """ECP-EML-11: Invalid space character in domain."""
        result = validators.email("user@ex ample.com")
        assert isinstance(result, ValidationError)
        assert bool(result) is False

    # ------------------------------------------------------------------------
    # Task 4: Parameterized Data-Driven Test Suite for email syntax variations
    # ------------------------------------------------------------------------
    @pytest.mark.order(35)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    @pytest.mark.parametrize(
        "email_address,expected_valid",
        [
            ("valid.first@company.co.uk", True),
            ("valid_underscore@sub.domain.org", True),
            ("plainaddress", False),
            ("@missingusername.com", False),
            ("username@.com", False),
            ("user@domain..com", False),
        ],
        ids=["uk_tld", "underscore_subdomain", "no_at", "no_user", "leading_dot_domain", "consecutive_dots"]
    )
    def test_email_parameterized_syntax(self, email_address, expected_valid):
        """Task 4: Parameterized test evaluating varied valid and invalid RFC email formats."""
        result = validators.email(email_address)
        if expected_valid:
            assert result is True
        else:
            assert isinstance(result, ValidationError)
            assert bool(result) is False
