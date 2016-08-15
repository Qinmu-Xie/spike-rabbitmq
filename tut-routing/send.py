import pika
import sys

serverity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='direct-logs', type='direct')
channel.basic_publish(exchange='direct-logs',
                      routing_key=serverity,
                      body=message)
print(" [X] Sent %r:%r" % (serverity, message))
connection.close()
