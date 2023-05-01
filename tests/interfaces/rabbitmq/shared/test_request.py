# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    25/09/2018
    Description:
    
"""

import pytest
from src.interfaces.rabbitmq.shared.request import Request


def test_request_routing_key_valid():
    msg = b'{}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert request.module_ == 'app'
    assert request.action_ == 'test'


def test_request_routing_key_with_region_valid():
    msg = b'{}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert request.module_ == 'app'
    assert request.action_ == 'test'


def test_request_routing_key_too_small():
    msg = b'{}'
    routing_key = 'igrec.app.test'
    reply_to = ''
    with pytest.raises(ValueError, message='Value Error expected'):
        Request(routing_key, reply_to, msg)


def test_request_routing_key_not_for_igrec():
    msg = b'{}'
    routing_key = 'igrec.app.test'
    reply_to = ''
    with pytest.raises(ValueError, message='Value Error expected'):
        Request(routing_key, reply_to, msg)


def test_request_msg_is_object():
    msg = b'{"mac" : "00:11:22:33:44:55"}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert request.msg_['mac'] == '00:11:22:33:44:55'


def test_request_msg_is_list():
    msg = b'[{"ip": "192.168.1.1", "mac": "01:11:22:33:44:55"}, {"ip": "192.168.1.2", "mac": "02:11:22:33:44:55"}, {"ip": "192.168.1.3", "mac": "03:11:22:33:44:55"}]'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert len(request.msg_) == 3


def test_request_msg_is_empty():
    msg = b'{}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert type(request.msg_) is dict


def test_request_msg_is_invalid():
    msg = b'{[{"ip": "192.168.1.1", "mac": "01:11:22:33:44:55"}, {"ip": "192.168.1.1", "mac": "01:11:22:33:44:55"}]}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    with pytest.raises(ValueError, message='Value Error expected'):
        Request(routing_key, reply_to, msg)


def test_request_msg_is_not_str():
    msg = b'{}'
    routing_key = 'igrec.app.test.igrec'
    reply_to = ''
    request = Request(routing_key, reply_to, msg)
    assert type(request.msg_) is dict
