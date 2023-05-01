from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request():
    from . import ips, config
    resp = DataObject()
    dump = ips.list(name=config.get_config('ipset.authlist'))
    if len(dump):
        maclist = dump[0].get_attr('IPSET_ATTR_ADT')['attrs']
        for macdata in maclist:
            mac = macdata.get_value().get_attr('IPSET_ATTR_ETHER')
            if mac is not None:
                resp.add_data({'mac': mac})
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
