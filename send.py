#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

name = ' '.join(sys.argv[1:])

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello '+ name)
print " [x] Sent Hello "+ name
connection.close()
