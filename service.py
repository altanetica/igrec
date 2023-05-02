#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import sys
import time
from src.interfaces import rpc
from src.use_cases import startup
from src.settings import GlobalConfig


def main():
    logging.warning("System start")
    threads = []
    try:
        config = GlobalConfig('config.toml')
        startup.load_arp(config.get_config('local.interfaces.internal'), config.get_config('staticarp.filename'))
        threads = rpc.run()
        while True:
            time.sleep(1000)
    except (KeyboardInterrupt, SystemExit):
        for t in threads:
            t.join(5)
        logging.warning("System exit")
        sys.exit(0)


if __name__ == '__main__':
    main()
