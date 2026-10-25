# Tests for Module 2: domain validator
# Saim Naveed (24F-3043)

import pytest
import validators
from validators import ValidationError


@pytest.mark.order(36)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.smoke
@pytest.mark.ecp
def test_domain_standard_valid():
    # regular .com domain
    assert validators.domain("google.com") is True


@pytest.mark.order(37)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_country_code_tld():
    # country code tld
    assert validators.domain("bbc.co.uk") is True


@pytest.mark.order(38)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_nested_subdomain():
    # multi-level subdomains
    assert validators.domain("dev.portal.example.org") is True


@pytest.mark.order(39)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_with_hyphen():
    # hyphen inside label
    assert validators.domain("my-cool-site.net") is True


@pytest.mark.order(40)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_missing_tld():
    # single label with no tld
    res = validators.domain("localhost")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(41)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_leading_hyphen_invalid():
    # cannot start label with a dash
    res = validators.domain("-example.com")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(42)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_trailing_hyphen_invalid():
    # cannot end label with a dash
    res = validators.domain("example-.com")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(43)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
def test_domain_invalid_chars():
    # underscore and space are illegal in domain names
    assert isinstance(validators.domain("bad_domain.com"), ValidationError)
    assert isinstance(validators.domain("bad domain.com"), ValidationError)


@pytest.mark.order(44)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.bva
def test_domain_bva_single_char_label():
    # minimum 1 character label
    assert validators.domain("a.com") is True


@pytest.mark.order(45)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.bva
def test_domain_bva_label_length_63_and_64():
    # max label length is 63 chars (RFC 1034)
    label_63 = ("a" * 63) + ".com"
    label_64 = ("a" * 64) + ".com"

    assert validators.domain(label_63) is True
    assert isinstance(validators.domain(label_64), ValidationError)


@pytest.mark.order(46)
@pytest.mark.saim_suite
@pytest.mark.domain_suite
@pytest.mark.ecp
@pytest.mark.parametrize(
    "domain_name,expected_valid",
    [
        ("github.com", True),
        ("fast.nu.edu.pk", True),
        ("invalid..double-dot.com", False),
        ("http://wrong-protocol.com", False),
        ("", False),
    ],
    ids=["github", "pk_domain", "double_dot", "with_protocol", "empty_string"]
)
def test_domain_parameterized(domain_name, expected_valid):
    res = validators.domain(domain_name)
    if expected_valid:
        assert res is True
    else:
        assert isinstance(res, ValidationError)
        assert bool(res) is False
