from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request():
    from . import ips, config
    resp = DataObject()
    ips.flush(name=config.get_config('ipset.keepttl'))
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
