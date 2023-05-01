# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    26/09/2018
    Description:
    
"""

# todo: in development

from threading import Thread, Event

from src.settings import GlobalConfig


class RabbitMQThread(Thread):
    def __init__(self, callback, *args, **kwargs):
        super(RabbitMQThread, self).__init__(*args, **kwargs)
        self.callback = callback
        self.config = GlobalConfig().get_config('rpc.rabbitmq')  # type: dict
        self._stopRequest = Event()
