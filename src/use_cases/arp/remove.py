from src.interfaces.zeromq.shared.dataobject import DataObject
from src.models.macaddr import MacAddr
from src.models.ipaddr import IpAddr
from . import ipr, iface, NetlinkError


def process_request(ipaddr=None, mac=None):
    if ipaddr is None and mac is None:
        return None
    try:
        if ipaddr is None or mac is None:
            if mac is None:
                r = ipr.neigh('dump', ifindex=iface, dst=ipaddr)
            else:
                r = ipr.neigh('dump', ifindex=iface, lladdr=mac)
            if len(r):
                ipaddr = r[0].get_attr('NDA_DST')
                mac = r[0].get_attr('NDA_LLADDR')
        ipr.neigh('del', dst=ipaddr, lladdr=mac, ifindex=iface)
    except NetlinkError as e:
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
            ip = None
            mac = None
            if hasattr(d, 'ip'):
                ip = IpAddr(d.ip).to_str()
            if hasattr(d, 'mac'):
                mac = MacAddr(d.mac).to_str().lower()
            r = process_request(ip, mac)
            resp.add_data(r)
        except (ImportError, AttributeError, TypeError, ValueError) as e:
            resp.add_error(d.__str__(), str(e))
    return resp
