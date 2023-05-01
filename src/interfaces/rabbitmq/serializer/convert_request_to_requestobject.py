# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    24.09.2018
    Description:
    
"""

from src.interfaces.rabbitmq.shared.request import Request
from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.dataobject import DataObject


def request_to_requestobject(request):
    """
    :type request: Request
    """
    return RequestObject(request.module_, request.action_, DataObject(request.msg_))
