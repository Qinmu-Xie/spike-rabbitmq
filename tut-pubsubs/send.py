import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [X] Sent %r" % message)
connection.close()
