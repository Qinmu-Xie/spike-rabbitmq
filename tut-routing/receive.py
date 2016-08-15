import pika
import time
import sys


def callback(ch, method, properties, body):
    print(" [X] Received %r:%r" % (method.routing_key, body))
    time.sleep(body.count(b'.'))
    print(" [X] Done")

serverities = sys.argv[1:]
if not serverities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='direct-logs', type='direct')
result = channel.queue_declare(exclusive=True)
for serverity in serverities:
    channel.queue_bind(exchange='direct-logs',
                       queue=result.method.queue,
                       routing_key=serverity)

channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=True)
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
