import pika
import time


def callback(ch, method, properties, body):
    print(" [X] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [X] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
channel.basic_consume(callback,
                      queue='task_queue')
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
