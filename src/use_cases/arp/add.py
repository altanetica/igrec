from src.interfaces.zeromq.shared.dataobject import DataObject
from src.models.macaddr import MacAddr
from src.models.ipaddr import IpAddr
from . import ipr, iface, NetlinkError


def process_request(ipaddr, mac):
    try:
        ipr.neigh('change', ifindex=iface,
                lladdr=mac,
                dst=ipaddr,
                nud='permanent')
    except NetlinkError, e:
        pass
    return {'ip': ipaddr, 'mac': mac}


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
            ip = IpAddr(d.ip).to_str()
            mac = MacAddr(d.mac).to_str().lower()
            r = process_request(ip, mac)
            resp.add_data(r)
        except (ImportError, AttributeError, TypeError, ValueError), e:
            resp.add_error(d.__str__(), e.message)
    return resp
