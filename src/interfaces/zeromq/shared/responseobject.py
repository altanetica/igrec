import jsonschema
import json
from src.interfaces.zeromq.shared.dataobject import DataObject
from src.interfaces.zeromq.serializer.responseobject_serializer import ResponseObjectEncoder

RESPONSE_SCHEMA = {
    'type': 'object',
    'properties': {
        'code': {'type': 'number'},
        'models': {'type': ['object', 'null', 'array']},
        'errors': {'type': ['object', 'null', 'array']},
    },
    'required': ['code', 'models', 'errors'],
}

# todo: do refectoring
'''
    {
        "title": "JSON schema for Bower configuration files",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "anyOf" : [
            {
              "type": "object",
              "properties" : {
                    "ip" : {"type": "string"},
                },
              "required": ["ip"]
            },
            {
              "type": "array",
              "items": {
                "type": "object",
                "properties" : {
                    "ip" : {"type": "string"},
                    },
                "required": ["ip"]
                },
            }
         ]
    }
'''

CODE_SUCCESS = 0
CODE_WITH_ERRORS = 1
CODE_FAIL = -1


class ResponseObject(object):
    def __init__(self, code, response):
        self.code = code
        self.response = response

    def to_str(self):
        return "code: " + self.code + ", models: " + \
               self.response.data.__str__() + ", errors: " + \
               self.response.errors.__str__()

    def to_json(self):
        try:
            jsn = json.dumps(self, cls=ResponseObjectEncoder)
            jsonschema.validate(json.loads(jsn), RESPONSE_SCHEMA)
        except (TypeError, jsonschema.ValidationError) as e:
            return json.dumps({'code': CODE_FAIL, 'models': None,
                               'errors': [{'param': 'ResponseObject', 'message': str(e)}]})
        return jsn

    def get_response(self):
        return self.response


class ResponseSuccess(ResponseObject):
    def __init__(self, response):
        if not isinstance(response, DataObject):
            response = DataObject(response)
        if response.has_errors():
            ResponseObject.__init__(self, CODE_WITH_ERRORS, response)
        else:
            ResponseObject.__init__(self, CODE_SUCCESS, response)


class ResponseFail(ResponseObject):
    def __init__(self, param, message):
        response = DataObject()
        response.add_error(param, message)
        ResponseObject.__init__(self, CODE_FAIL, response)
