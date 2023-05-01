from src.interfaces.zeromq.shared.dataobject import DataObject
from src.interfaces.zeromq.serializer.dataobject_serializer import DataObjectEncoder


def test_dataobject_serializer():
    data = DataObject()
    data.add_data({'ping': '1'})
    data.add_error('error', 'message')
    assert DataObjectEncoder().default(data) == {'models': {'ping': '1'}, 'errors': [{'message': 'message', 'param': 'error'}]}
