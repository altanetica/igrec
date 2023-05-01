# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    24.09.2018
    Description:
    
"""

from src.interfaces.rabbitmq.shared.response import ResponseError, ResponseSuccess
from src.interfaces.zeromq.shared.responseobject import ResponseObject, CODE_FAIL


def responseobject_to_response(robject):
    """
    :type robject: ResponseObject
    """
    if robject.code == CODE_FAIL:
        response = ResponseError(101, robject.response.errors.__str__())
    else:
        # need fix
        rdata = robject.response
        try:
            if rdata.is_empty():
                data = None
            elif len(rdata.data) == 1:
                d = rdata.data[0]
                data = d.__dict__
            else:
                data = []
                for d in rdata.data:
                    data.append(d.__dict__)
        except AttributeError:
            data = None
        response = ResponseSuccess(data=data)
    return response
