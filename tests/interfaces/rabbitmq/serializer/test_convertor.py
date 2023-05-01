# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    27/09/2018
    Description:
    
"""

from src.interfaces.rabbitmq.shared.request import Request
from src.interfaces.rabbitmq.serializer.convert_request_to_requestobject import request_to_requestobject
from src.interfaces.zeromq.shared.requestobject import RequestObject


def test_convertor_request_to_requestobject():
    msg = b'[{"ip": "127.0.0.1"}, {"ip": "127.0.0.2"}]'
    key = 'igrec.app.test.igrec.dev'
    request = Request(key, '', msg)
    robject = request_to_requestobject(request)  # type: RequestObject
    assert len(robject.data.data) == 2
    assert robject.module_ == 'app'
    assert robject.action == 'test'
