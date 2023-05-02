from src.interfaces.zeromq.shared.dataobject import DataObject
from src.models.macaddr import MacAddr


def process_request(mac):
    from . import ips, config
    if ips.test(config.get_config('ipset.authlist'), mac, etype='mac'):
        ips.delete(config.get_config('ipset.authlist'), mac, etype='mac')
    return {'mac': mac}


def execute(data):
    """
    :param data:
    :type data: DataObject
    """
    if not isinstance(data, DataObject):
        raise ValueError
    resp = DataObject()
    for err in data.errors:
        resp.add_error(err.param, err.message)
    if data.is_empty():
        return resp
    for d in data.data:
        try:
            mac = MacAddr(d.mac).to_str().lower()
            r = process_request(mac)
            resp.add_data(r)
        except (ImportError, AttributeError, TypeError, ValueError) as e:
            resp.add_error(d.__str__(), str(e))
    return resp
