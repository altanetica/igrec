#!/usr/bin/env python

import zmq
import time
import random
import datetime


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.REQ)
    zmq_socket.connect("tcp://127.0.0.1:5559")
    while True:
        num = random.randrange(100)
        work_message = {'module': 'app', 'action': 'check', 'models': [{'ping': num}]}
        zmq_socket.send_json(work_message)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        print('send:'),
        print(num)
        message = zmq_socket.recv()
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        print('recieve:'),
        print(message)
        time.sleep(60)


if __name__ == '__main__':
    producer()
