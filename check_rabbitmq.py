#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    03/10/2018
    Description:
    
"""

import pika
import time
import random
import datetime


def check_status():
    while True:
        num = random.randrange(100)
        work_message = {'module': 'app', 'action': 'check', 'models': [{'ping': num}]}
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        print('send:'),
        print(num)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        print('recieve:'),
        time.sleep(60)


if __name__ == '__main__':
    check_status()
