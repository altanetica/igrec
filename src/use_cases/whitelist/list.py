from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request():
    from . import ips, config
    resp = DataObject()
    dump = ips.list(name=config.get_config('ipset.whitelist'))
    if len(dump):
        iplist = dump[0].get_attr('IPSET_ATTR_ADT')['attrs']
        for ipdata in iplist:
            ipaddr = ipdata.get_value().get_attr('IPSET_ATTR_IP_FROM').get_attr('IPSET_ATTR_IPADDR_IPV4')
            resp.add_data({'ip': ipaddr})
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
