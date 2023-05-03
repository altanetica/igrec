from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request(msg):
    return msg


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
    for d in data.data:
        try:
            msg = d.ping
            resp.add_data({'pong': process_request(msg)})
        except (ImportError, AttributeError, TypeError, ValueError) as e:
            resp.add_error(d.__str__(), str(e))
    return resp
