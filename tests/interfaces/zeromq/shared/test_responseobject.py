from src.interfaces.zeromq.shared.responseobject import ResponseObject
from src.interfaces.zeromq.shared.dataobject import DataObject


def test_responseobject_empty():
    data = DataObject()
    r = ResponseObject(0, data)
    assert r.to_json() == '{"code": 0, "models": null, "errors": null}'


def test_responseobject_nonempty():
    data = DataObject()
    data.add_data({'ping': '1'})
    data.add_error('error', 'message')
    r = ResponseObject(1, data)
    assert r.to_json() == '{"code": 1, "models": {"ping": "1"}, "errors": [{"message": "message", "param": "error"}]}'
