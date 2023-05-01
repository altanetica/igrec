from src.interfaces.zeromq.shared.responseobject import ResponseObject
from src.interfaces.zeromq.shared.dataobject import DataObject
from src.interfaces.zeromq.serializer.responseobject_serializer import ResponseObjectEncoder


def test_responseobject_serializer():
    data = DataObject()
    data.add_data({'ping': '1'})
    data.add_error('error', 'message')
    r = ResponseObject(1, data)
    assert ResponseObjectEncoder().default(r) == {'code': 1, 'models': {'ping': '1'}, 'errors': [{'message': 'message', 'param': 'error'}]}
