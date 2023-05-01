# -*- coding: UTF-8 -*-
"""
    Unit Test Lab
    26/09/2018
    Description:
    
"""

# todo: in development

import pika
from src.settings import GlobalConfig


from rabbitmqinterface import RabbitMQInterface


class RabbitMQBlocked(RabbitMQInterface):
    def __init__(self):
        super(RabbitMQBlocked, self).__init__()
        self.config = GlobalConfig().get_config('rpc.rabbitmq')  # type: dict
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['host'],
                                                                            port=self.config['port'],
                                                                            credentials=pika.PlainCredentials(self.config['username'], self.config['password'])))
        self.exchange = self.config['exchange']
        self.routing_key = self.config['key'] + self.config['region']

        self.channel_number = 0

    def run(self):
        channel = self.connection.channel()
        self.channel_number = channel.channel_number
        # channel.exchange_declare(app.exchange, 'topic', False, False, False)
        queue = channel.queue_declare(exclusive=True)
        channel.basic_consume(self.on_request, queue=queue)
        channel.queue_bind(queue=queue, exchange=self.exchange, routing_key=self.routing_key)
        channel.start_consuming()
        pass

    def stop(self):
        channel = self.connection.channel(self.channel_number)
        channel.close()
        self.connection.close()
        pass

    def on_request(self, channel, method, props, body):
        """
        Прием сообщения
        :type channel: pika.Channel
        :type method: pika.spec.Basic.Deliver
        :type props: pika.spec.BasicProperties
        :type body: str
        """
        pass

    def send_response(self, channel, props, method, response):
        """
        Sender
        :type channel: pika.Channel
        :type method: pika.spec.Basic.Deliver
        :type props: pika.spec.BasicProperties
        :type response: str
        """
        channel.basic_publish(exchange='',
                              routing_key=props.reply_to,
                              properties=pika.BasicProperties(correlation_id=props.correlation_id),
                              body=str(response))
        channel.basic_ack(delivery_tag=method.delivery_tag)
        pass
