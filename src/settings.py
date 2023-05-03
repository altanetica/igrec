# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    05.03.2018
"""

import logging
import toml


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


__DEFAULT_CONFIG__ = "default.toml"
__WORKING_CONFIG__ = "config.toml"


class GlobalConfig:
    """
    Singleton with global configuration
    """
    __metaclass__ = Singleton

    def __init__(self, fname=__WORKING_CONFIG__):
        self.logger = logging.getLogger(__name__)
        self.config = dict()
        self.config_load(__DEFAULT_CONFIG__)
        self.config_load(fname)
        pass

    def config_load(self, fname):
        """
        Загрузка настроек из конфигурационного файла
        """
        try:
            with open(fname, "r") as f:
                # update dict with new values
                self.config.update(toml.load(f))
        except toml.TomlDecodeError:
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

    def dump(self):
        return toml.dumps(self.config)


def print_default():
    with open(__DEFAULT_CONFIG__, "r") as f:
        try:
            print(toml.dumps(toml.load(f)))
        except toml.TomlDecodeError:
            print("Error at load default config file.")


def print_config(fname):
    try:
        print(toml.dumps(toml.load([__DEFAULT_CONFIG__, fname])))
    except toml.TomlDecodeError:
        print("Error at load config file.")
