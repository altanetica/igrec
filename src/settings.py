#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    05.03.2018
"""

import logging
import yaml
from src.utils.singleton import Singleton


class GlobalConfig:
    """
    Singleton with global configuration
    """
    __metaclass__ = Singleton

    def __init__(self, fname='config.yaml'):
        self.logger = logging.getLogger(__name__)
        self.config = dict()
        self.config_load('default.config.yaml')
        self.config_load(fname)
        pass

    def config_load(self, fname):
        """
        Загрузка настроек из конфигурационного файла
        """
        try:
            with open(fname, "r") as f:
                # update dict with new values
                self.config.update(yaml.load(f))
        except ImportError:
            self.logger.error("Error at load confg file.")

    def get_config(self, key=None):
        return self.get_value(key=key)

    def get_value(self, key=None):
        if key is None:
            return self.config
        else:
            keys = key.split('.')
            cfg = self.config
            for k in keys:
                cfg = cfg.get(k)
                if cfg is None:
                    break
            return cfg


def print_default():
    with open("default.config.yaml", 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as e:
            print(e)


def print_config(fname):
    config = dict()
    with open("default.config.yaml", 'r') as stream:
        try:
            config.update(yaml.load(stream))
        except yaml.YAMLError as e:
            print(e)
    with open(fname, 'r') as stream:
        try:
            config.update(yaml.load(stream))
        except yaml.YAMLError as e:
            print(e)
    print(config)


if __name__ == '__main__':
    print_config('config.yaml')
