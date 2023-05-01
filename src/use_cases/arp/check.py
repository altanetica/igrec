# -*- coding: UTF-8 -*-
from src.interfaces.zeromq.shared.dataobject import DataObject
from src.models.macaddr import MacAddr
from src.models.ipaddr import IpAddr
from . import ipr, iface, NetlinkError, VALID_MAC_STATES


def process_request(ipaddr=None, mac=None):
    r = list()
    try:
        if ipaddr is None:
            if mac is None:
                return None
            else:
                r = ipr.neigh('dump', ifindex=iface, lladdr=mac)
        else:
            r = ipr.neigh('dump', ifindex=iface, dst=ipaddr)
    except NetlinkError, e:
        pass
    '''
    else:
        if mac is None:
            r = ipr.neigh('dump', ifindex=iface, dst=ipaddr)
        else:
            r = ipr.neigh('dump', ifindex=iface, dst=ipaddr, lladdr=mac)
    '''
    if len(r):
        mac = r[0].get_attr('NDA_LLADDR')
        ip = r[0].get_attr('NDA_DST')
        state = r[0]['state']
        # фильтруем маки
        if state in VALID_MAC_STATES:
            return {'mac': mac, 'ip': ip, 'state': state}
    return None


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
        except (ImportError, AttributeError, TypeError, ValueError), e:
            resp.add_error(d.__str__(), e.message)
    return resp
