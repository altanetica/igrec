from src.interfaces.zeromq.shared.dataobject import DataObject
import logging


def process_request():
    import iptc
    from src.settings import GlobalConfig
    config = GlobalConfig()
    resp = DataObject()
    # changettl
    table = iptc.Table(iptc.Table.MANGLE)
    chain = iptc.Chain(table=table, name=config.get_config('iptables.chains.ttl'))
    for rule in chain.rules:
        if rule.target == iptc.Target(rule, "RETURN"):
            if not len(rule.matches):
                nrule = iptc.Rule()
                target = iptc.Target(rule, "TTL")
                target.ttl_set = "1"
                nrule.target = target
                chain.delete_rule(rule)
                chain.append_rule(nrule)
                break
    # authlist
    table = iptc.Table(iptc.Table.MANGLE)
    chain = iptc.Chain(table=table, name=config.get_config('iptables.chains.auth'))
    for rule in chain.rules:
        if rule.target == iptc.Target(rule, "RETURN"):
            nrule = iptc.Rule()
            target = iptc.Target(nrule, "MARK")
            target.set_mark = "0x22"
            nrule.target = target
            chain.delete_rule(rule)
            chain.insert_rule(nrule)
            break
    # whitelist
    table = iptc.Table(iptc.Table.MANGLE)
    chain = iptc.Chain(table=table, name=config.get_config('iptables.chains.white'))
    for rule in chain.rules:
        if rule.target == iptc.Target(rule, "RETURN"):
            nrule = iptc.Rule()
            nrule.target = iptc.Target(nrule, "ACCEPT")
            m = nrule.create_match("set")
            m.match_set = [config.get_config('ipset.whitelist'), 'dst']
            chain.delete_rule(rule)
            chain.insert_rule(nrule)
            break
    logging.warning("system enabled")
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
