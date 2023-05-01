from src.interfaces.zeromq.shared.dataobject import DataObject
from src.models.ipaddr import IpAddr


def process_request(ipaddr):
    from . import ips, config
    if not ips.test(config.get_config('ipset.keepttl'), ipaddr):
        ips.add(config.get_config('ipset.keepttl'), ipaddr)
    return {'ip': ipaddr}


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
            ipaddr = IpAddr(d.ip).to_str()
            r = process_request(ipaddr)
            resp.add_data(r)
        except (ImportError, AttributeError, TypeError, ValueError), e:
            resp.add_error(d.__str__(), e.message)
    return resp
