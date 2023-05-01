# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    24.09.2018
    Description:
    
"""

import json


class Request(object):
    def __init__(self, routing_key, reply_to, msg):
        self.module_, self.action_ = self.routing_to_cmd(routing_key)
        self.reply_to_ = reply_to
        self.msg_ = self.load_msg(msg)

    @staticmethod
    def routing_to_cmd(routing_key):
        cmd = routing_key.split('.')
        if len(cmd) < 4:
            raise ValueError
        # todo: remove ???
        if cmd[0] != 'igrec':
            raise ValueError
        return cmd[1], cmd[2]

    @staticmethod
    def load_msg(msg):
        if type(msg) is str:
            return json.loads(msg)
        return msg
