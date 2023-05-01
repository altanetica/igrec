import pytest
from src.models.macaddr import MacAddr


def test_macaddr_init():
    mac = MacAddr('00:11:22:33:44:55')
    assert mac.to_str() == '00:11:22:33:44:55'
    mac = MacAddr('66:11:22:33:44:55')
    assert mac.to_str() == '66:11:22:33:44:55'
    mac = MacAddr('AA-FF-00-33-1B-DD')
    assert mac.to_str() == 'aa:ff:00:33:1b:dd'


def test_macaddr_fail_init():
    with pytest.raises(ValueError):
        MacAddr('XX:00:00:00:00:00')
    with pytest.raises(ValueError):
        MacAddr('11:00:00:00:00:00:11')
    with pytest.raises(ValueError):
        MacAddr('256.256.256.256')
    with pytest.raises(ValueError):
        MacAddr('00:00:00:00:00:00')
    with pytest.raises(ValueError):
        MacAddr('ff:ff:ff:ff:ff:ff')
