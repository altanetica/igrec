#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    2/5/23
    Description:
    
"""

import argparse

from scripts import system_enable, system_disable, check_zeromq, print_config

__SCRIPTS__ = {
    'enable': system_enable.system_enable,
    'disable': system_disable.system_disable,
    'check': check_zeromq.check_zeromq,
    'config': print_config.print_config,
    'test': lambda: print('test'),
    'status': lambda: print('status'),
    'setup': lambda: print('setup')
}


def main(fn: str):
    try:
        __SCRIPTS__[fn]()
    except KeyError:
        pass
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IGREC Service')
    parser.add_argument('action', choices=['enable', 'disable', 'check', 'test', 'status', 'setup', 'config'])
    args = parser.parse_args()
    main(args.action)
