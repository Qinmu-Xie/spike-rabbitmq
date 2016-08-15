import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='121.42.153.143', port=5672))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, World!')
print(" [X] Sent 'Hello, World!'")
connection.close()
