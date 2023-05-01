# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    27/09/2018
    Description:
    
"""

import json


class DataEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {}
            if isinstance(o, list) or isinstance(o, dict):
                to_serialize = {'models': o}
            return to_serialize
        except AttributeError:
            return json.JSONEncoder().default(o)


class ResponseSuccessEncoder(json.JSONEncoder):
    def default(self, o):
        """
        :type o: src.interfaces.rabbitmq.shared.response.Response
        """
        try:
            data = DataEncoder().default(o.data)
            to_serialize = {
                'result': 'ok',
            }
            to_serialize.update(data)
            return to_serialize
        except AttributeError, e:
            return json.JSONEncoder().default(o)


class ResponseErrorEncoder(json.JSONEncoder):
    def default(self, o):
        """
        :type o: src.interfaces.rabbitmq.shared.response.Response
        """
        try:
            to_serialize = {
                'result': 'error',
                'code':  o.code,
                'message': o.message
            }
            return to_serialize
        except AttributeError, e:
            return json.JSONEncoder().default(o)
