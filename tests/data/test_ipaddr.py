import pytest
from src.models.ipaddr import IpAddr


def test_ipaddr_init():
    ip = IpAddr(0)
    assert ip.to_int() == 0
    ip = IpAddr('0.0.0.0')
    assert ip.to_int() == 0
    ip = IpAddr('127.0.0.1')
    assert ip.to_int() == 2130706433
    assert ip.to_str() == "127.0.0.1"
    ip = IpAddr('185.10.82.95')
    assert ip.to_int() == 3104461407
    ip = IpAddr(3104460801)
    assert ip.to_str() == "185.10.80.1"


def test_ipaddr_fail_init():
    with pytest.raises(ValueError):
        IpAddr(-5)
    with pytest.raises(ValueError):
        IpAddr('256.256.256.256')
