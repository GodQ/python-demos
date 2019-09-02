import pika
import time

host = "192.168.99.100"
port = 30567
def connect():
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        credentials=credentials,
        host=host,
        port=port))
    return connection

def send():
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def recv():
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    send()
    recv()
