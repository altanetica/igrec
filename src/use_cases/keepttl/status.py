from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request():
    from . import config
    import iptc
    resp = DataObject()
    table = iptc.Table(iptc.Table.MANGLE)
    chain = iptc.Chain(table=table, name=config.get_config('iptables.chains.ttl'))
    status = 'enabled'
    for rule in chain.rules:
        target = iptc.Target(rule, "TTL")
        target.ttl_set = "1"
        if rule.target == target:
            if len(rule.matches):
                status = 'disabled'
    resp.add_data({'status': status})
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
