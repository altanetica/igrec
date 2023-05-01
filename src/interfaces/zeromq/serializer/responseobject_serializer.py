import json
from src.interfaces.zeromq.serializer.dataobject_serializer import DataObjectEncoder


class ResponseObjectEncoder(json.JSONEncoder):
    def default(self, o):
        """
        :type o: shared.responseobject.ResponseObject
        """
        try:
            resp = DataObjectEncoder().default(o.response)
            to_serialize = {
                'code': o.code,
            }
            to_serialize.update(resp)
            return to_serialize
        except AttributeError, e:
            return json.JSONEncoder().default(o)
