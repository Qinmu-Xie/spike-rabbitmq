import pika


def callback(ch, method, properties, body):
    print (" [X] Received %r" % body)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
