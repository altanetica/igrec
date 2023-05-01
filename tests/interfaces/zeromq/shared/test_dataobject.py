from src.interfaces.zeromq.shared.dataobject import DataObject


def test_dataobject_valid():
    jsn = {'models': {'ip': '192.168.1.1', 'mac': '00:11:22:33:44:55'}}
    data = DataObject(jsn['models'])
    assert data.is_valid()
    assert len(data.data) == 1
    assert not data.is_empty()
    assert not data.has_errors()


def test_dataobject_list():
    jsn = {'models': [{'ip': '192.168.1.1', 'mac': '01:11:22:33:44:55'},
                    {'ip': '192.168.1.2', 'mac': '02:11:22:33:44:55'},
                    {'ip': '192.168.1.3', 'mac': '03:11:22:33:44:55'}]}
    data = DataObject(jsn['models'])
    assert data.is_valid()
    assert len(data.data) == 3
    assert not data.is_empty()
    assert not data.has_errors()


def test_dataobject_empty():
    jsn = {'models': None}
    data = DataObject(jsn['models'])
    assert data.is_empty()
    assert not data.has_errors()


def test_dataobject_invalid():
    jsn = {'models': ''}
    data = DataObject(jsn['models'])
    assert not data.is_valid()
    assert data.is_empty()


def test_dataobject_empty_list():
    jsn = {'models': {'192.168.1.1'}}
    data = DataObject(jsn['models'])
    assert data.is_empty()
    assert data.has_errors()


def test_dataobject_list_with_not_valid():
    jsn = {'models': [None,
                    {'ip': '192.168.1.1', 'mac': '01:11:22:33:44:55'},
                    None,
                    {'192.168.1.1'}]}
    data = DataObject(jsn['models'])
    assert data.is_valid() is False
    assert data.has_errors() is True


def test_dataobject_list_with_all_not_valid():
    jsn = {'models': [None,
                    {'192.168.1.1'}]}
    data = DataObject(jsn['models'])
    assert data.is_empty() is True
    assert data.has_errors() is True
