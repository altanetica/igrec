from src.interfaces.zeromq.shared.dataobject import DataObject
from . import ipr, iface


def process_request():
    resp = DataObject()
    dump = ipr.get_neighbours(ifindex=iface, match=lambda x: x['state'] in (2, 128))
    resp.add_data({'count': len(dump)})
    return resp


def execute(data):
    """
    :param data:
    :type data: DataObject
    """
    if not isinstance(data, DataObject):
        raise ValueError
    resp = process_request()
    for err in data.errors:
        resp.add_error(err.param, err.message)
    return resp
