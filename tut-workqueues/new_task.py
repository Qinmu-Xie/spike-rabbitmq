import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode=2
                      ))
print(" [X] Sent %r" % message)
connection.close()
