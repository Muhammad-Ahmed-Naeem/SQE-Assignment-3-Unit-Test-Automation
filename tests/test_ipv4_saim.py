# Tests for Module 3: ipv4 validator
# Saim Naveed (24F-3043)

import pytest
import validators
from validators import ValidationError


@pytest.mark.order(47)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.smoke
@pytest.mark.ecp
def test_ipv4_standard_valid():
    # regular public ip
    assert validators.ipv4("8.8.8.8") is True


@pytest.mark.order(48)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.ecp
def test_ipv4_private_class_c():
    # private range 192.168.x.x
    assert validators.ipv4("192.168.1.1") is True


@pytest.mark.order(49)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.ecp
def test_ipv4_loopback():
    # localhost
    assert validators.ipv4("127.0.0.1") is True


@pytest.mark.order(50)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.bva
def test_ipv4_min_boundary_all_zeros():
    # min possible octet value (0)
    assert validators.ipv4("0.0.0.0") is True


@pytest.mark.order(51)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.bva
def test_ipv4_max_boundary_255():
    # max possible octet value (255)
    assert validators.ipv4("255.255.255.255") is True


@pytest.mark.order(52)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.bva
def test_ipv4_above_max_octet_256():
    # octet 256 is out of 8-bit range
    res = validators.ipv4("256.0.0.1")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(53)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.bva
def test_ipv4_negative_octet():
    # negative octets are invalid
    res = validators.ipv4("-1.0.0.1")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(54)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.ecp
def test_ipv4_incomplete_octets():
    # missing 4th octet
    res = validators.ipv4("192.168.1")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(55)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.ecp
def test_ipv4_too_many_octets():
    # 5 octets provided
    res = validators.ipv4("192.168.1.1.1")
    assert isinstance(res, ValidationError)
    assert bool(res) is False


@pytest.mark.order(56)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.bva
def test_ipv4_cidr_boundaries():
    # /0 and /32 are valid CIDR limits; /33 is out of range
    assert validators.ipv4("10.0.0.0/0") is True
    assert validators.ipv4("10.0.0.1/32") is True
    assert isinstance(validators.ipv4("10.0.0.1/33"), ValidationError)


@pytest.mark.order(57)
@pytest.mark.saim_suite
@pytest.mark.network_suite
@pytest.mark.ecp
@pytest.mark.parametrize(
    "ip_address,expected_valid",
    [
        ("10.0.0.1", True),
        ("172.16.0.1", True),
        ("192.168.100.254", True),
        ("999.999.999.999", False),
        ("abc.def.ghi.jkl", False),
        ("", False),
    ],
    ids=["class_a", "class_b", "high_host", "overflow", "alpha", "empty"]
)
def test_ipv4_parameterized(ip_address, expected_valid):
    res = validators.ipv4(ip_address)
    if expected_valid:
        assert res is True
    else:
        assert isinstance(res, ValidationError)
        assert bool(res) is False
