# -*- coding: UTF-8 -*-
from src.interfaces.zeromq.shared.dataobject import DataObject
from . import ipr, iface, VALID_MAC_STATES


def process_request():
    resp = DataObject()
    for x in ipr.neigh('dump', ifindex=iface):
        mac = x.get_attr('NDA_LLADDR')
        ip = x.get_attr('NDA_DST')
        state = x['state']
        # фильтруем маки
        if state in VALID_MAC_STATES:
            r = {'mac': mac, 'ip': ip, 'state': state}
            resp.add_data(r)
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
