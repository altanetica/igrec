from src.interfaces.zeromq.shared.dataobject import DataObject
from . import ipr, iface


def process_request():
    import json
    state = 128
    fn = "/etc/ether"
    resp = DataObject()
    objects = []
    with open(fn, "w") as f:
        try:
            for x in ipr.neigh('dump', ifindex=iface):
                if x['state'] == state:
                    objects.append({'ip': x.get_attr('NDA_DST'), 'mac': x.get_attr('NDA_LLADDR')})
            json.dump(objects, f)
        except IOError:
            pass
        finally:
            f.close()
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
