import jsonschema
import json
from src.interfaces.zeromq.shared.dataobject import DataObject

REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'module': {'type': 'string'},
        'action': {'type': 'string'},
        'models': {'type': ['object', 'null', 'array']},
    },
    'required': ['module', 'action', 'models'],
}


class RequestObject(object):

    def __init__(self, module_, action, data):
        self.module_ = module_
        self.action = action
        if isinstance(data, DataObject):
            self.data = data
        else:
            self.data = DataObject(data)

    @classmethod
    def from_json(cls, jsn):
        try:
            jsn = json.loads(jsn)
            jsonschema.validate(jsn, REQUEST_SCHEMA)
            req = RequestObject(
                module_=jsn['module'],
                action=jsn['action'],
                data=jsn['models']
            )
            return req
        except jsonschema.ValidationError as e:
            print(e)
            raise ValueError(str(e))

    def to_str(self):
        return "module: " + self.module_ + ", action: " + self.action + ", models: " + self.data.__str__()

    def __str__(self):
        return self.to_str()
