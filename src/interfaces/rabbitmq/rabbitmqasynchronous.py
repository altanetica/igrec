# -*- coding: UTF-8 -*-
import logging
import pika

from src.settings import GlobalConfig
from shared.request import Request
from src.interfaces.rabbitmq.shared.response import Response
from src.interfaces.rabbitmq.serializer.convert_request_to_requestobject import request_to_requestobject
from src.interfaces.rabbitmq.serializer.convert_responseobject_to_response import responseobject_to_response
from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.responseobject import ResponseObject


class RabbitMQAsynchronous(object):
    def __init__(self, cb):
        self.callback = cb
        self.config = GlobalConfig().get_config('rpc.rabbitmq')  # type: dict
        self.exchange_name = self.config['exchange']
        self.routing_key = self.config['key']
        self.queue_name = self.config['queue']
        self.connection = None
        self.channel = None
        self.closing = False
        self.consumer_tag = None

    def start(self):
        self.run()

    def run(self):
        self.connection = self.connect()
        self.connection.ioloop.start()

    def stop(self):
        self.closing = True
        self.stop_consuming()
        self.connection.ioloop.start()
        pass

    def connect(self):
        return pika.SelectConnection(pika.ConnectionParameters(host=self.config['host'], port=self.config['port'], ssl=self.config['ssl'],  virtual_host=self.config['vhost'],
                                                               credentials=pika.PlainCredentials(self.config['username'], self.config['password']), heartbeat=30),
                                     on_open_callback=self.on_connection_open,
                                     on_open_error_callback=None, on_close_callback=None,
                                     stop_ioloop_on_close=False)

    def reconnect(self):
        self.connection.ioloop.stop()
        if not self.closing:
            self.connection = self.connect()
            self.connection.ioloop.start()

    def on_connection_open(self, connection):
        self.add_on_connection_close_callback()
        self.open_channel()

    def add_on_connection_close_callback(self):
        self.connection.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, connection, reply_code, reply_text):
        self.channel = None
        if self.closing:
            self.connection.ioloop.stop()
        else:
            self.connection.add_timeout(5, self.reconnect)

    def open_channel(self):
        self.connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        self.channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self.exchange_name)

    def add_on_channel_close_callback(self):
        self.channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        self.connection.close()

    def setup_exchange(self, exchange_name):
        self.channel.exchange_declare(callback=self.on_exchange_declared, exchange=exchange_name, exchange_type='topic', passive=False, durable=True, auto_delete=False)

    def on_exchange_declared(self, frame):
        self.setup_queue(self.queue_name)

    def setup_queue(self, queue_name):
        self.channel.queue_declare(callback=self.on_queue_declared, queue=queue_name, exclusive=False, durable=True, auto_delete=False)

    def on_queue_declared(self, method_frame):
        self.channel.queue_bind(callback=self.on_queue_binded, queue=self.queue_name, exchange=self.exchange_name, routing_key=self.routing_key)

    def on_queue_binded(self, frame):
        self.start_consuming()

    def start_consuming(self):
        self.add_on_cancel_callback()
        self.consumer_tag = self.channel.basic_consume(consumer_callback=self.on_request, queue=self.queue_name)

    def add_on_cancel_callback(self):
        self.channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        if self.channel:
            self.channel.close()

    def on_request(self, channel, method, props, body):
        """
        Прием сообщения
        :type channel: pika.Channel
        :type method: pika.spec.Basic.Deliver
        :type props: pika.spec.BasicProperties
        :type body: str
        """
        try:
            # logging.warn('request is: ' + body)
            request = Request(method.routing_key, props.reply_to, body)
            req = request_to_requestobject(request)  # type: RequestObject
            robject = self.callback(req)  # type: ResponseObject
            response = responseobject_to_response(robject)  # type: Response
            resp = response.to_json()  # type: str
            self.send_response(channel, props, method, resp)
            pass
        except ValueError, e:
            resp = "{'result': 'error', code: 102, message: 'value error'}"  # type: str
            self.send_response(channel, props, method, resp)
        except Exception, e:
            logging.exception(e)
            resp = "{'result': 'error', code: 103, message: 'unknown exception'}"
            self.send_response(channel, props, method, resp)

    def send_response(self, channel, props, method, response):
        """
        Sender
        :type channel: pika.Channel
        :type method: pika.spec.Basic.Deliver
        :type props: pika.spec.BasicProperties
        :type response: str
        """
        # logging.warn('answer is: ' + response)
        if props.reply_to and props.correlation_id:
            channel.basic_publish(exchange=self.exchange_name,
                                  routing_key=props.reply_to,
                                  properties=pika.BasicProperties(correlation_id=props.correlation_id),
                                  body=response)
        self.acknowledge_message(method.delivery_tag)

    def acknowledge_message(self, delivery_tag):
        self.channel.basic_ack(delivery_tag)

    def stop_consuming(self):
        if self.channel:
            self.channel.basic_cancel(self.on_canceled, self.consumer_tag)

    def on_canceled(self, frame):
        self.close_channel()

    def close_channel(self):
        self.channel.close()

    def close_connection(self):
        self.connection.close()
