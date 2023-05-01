# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    24.09.2018
    Description:
    
"""

import jsonschema
import json
import src.interfaces.rabbitmq.serializer.response_serializer as serializer


RESPONSE_SCHEMA = {
    'type': 'object',
    'properties': {
        'code': {'type': 'number'},
        'models': {'type': ['object', 'null', 'array']},
        'errors': {'type': ['object', 'null', 'array']},
    },
    'required': ['code', 'models', 'errors'],
}


class Response(object):
    def __init__(self, data=None, error=False, code=0, message=''):
        self.error = error
        self.code = code
        self.message = message
        self.data = data

    def to_str(self):
        if self.error:
            return "result: error, code: " + str(self.code) + ", message: " + self.message
        else:
            return "result: ok, models: " + str(self.data)

    # todo:
    def data_to_str(self):
        pass

    def to_json(self):
        try:
            if self.error:
                jsn = json.dumps(self, cls=serializer.ResponseErrorEncoder)
                # todo:
                # jsonschema.validate(json.loads(jsn), RESPONSE_SCHEMA)
            else:
                jsn = json.dumps(self, cls=serializer.ResponseSuccessEncoder)
                # todo:
                # jsonschema.validate(json.loads(jsn), RESPONSE_SCHEMA)
            return jsn
        except [TypeError, jsonschema.ValidationError], e:
            return json.dumps({'result': 'error', 'code': 101, 'message': 'json encoder error'})


class ResponseSuccess(Response):
    def __init__(self, data):
        Response.__init__(self, data, error=False, code=0, message='')


class ResponseError(Response):
    def __init__(self, code, message):
        Response.__init__(self, data=None, error=True, code=code, message=message)
