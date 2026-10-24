# Tests for Module 2: email validation
# M. Ahmad Naeem (23F-3113)

import pytest
import validators
from validators import ValidationError


class TestEmailAhmad:

    @pytest.mark.order(23)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.smoke
    @pytest.mark.ecp
    def test_email_standard(self):
        assert validators.email("test.user@example.com") is True

    @pytest.mark.order(24)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_subdomain(self):
        assert validators.email("ahmad.naeem@student.fast.edu.pk") is True

    @pytest.mark.order(25)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_special_characters(self):
        assert validators.email("ahmad+sqe_test@example-domain.org") is True

    @pytest.mark.order(26)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_numeric(self):
        assert validators.email("233113@domain123.com") is True

    @pytest.mark.order(27)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_missing_at(self):
        res = validators.email("ahmadnaeemexample.com")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(28)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_double_at(self):
        res = validators.email("ahmad@@example.com")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(29)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_no_user(self):
        res = validators.email("@example.com")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(30)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_no_domain(self):
        res = validators.email("ahmad@")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(31)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_username_max_64(self):
        # RFC 5321 max username limit is 64 characters
        username_64 = "a" * 64
        assert validators.email(f"{username_64}@example.com") is True

    @pytest.mark.order(32)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_username_above_max_65(self):
        # 65 characters exceeds RFC limit
        username_65 = "a" * 65
        res = validators.email(f"{username_65}@example.com")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

    @pytest.mark.order(33)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.bva
    def test_email_single_char_username(self):
        assert validators.email("a@example.com") is True

    @pytest.mark.order(34)
    @pytest.mark.ahmad_suite
    @pytest.mark.email_suite
    @pytest.mark.ecp
    def test_email_space_in_domain(self):
        res = validators.email("user@ex ample.com")
        assert isinstance(res, ValidationError)
        assert bool(res) is False

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
    def test_email_syntax_variations(self, email_address, expected_valid):
        result = validators.email(email_address)
        if expected_valid:
            assert result is True
        else:
            assert isinstance(result, ValidationError)
            assert bool(result) is False
