import pika
import time

# host = "172.29.80.126"
# port = 5672
# user = "aaa"
# password = "aaa"
# vhost = "/aaa"

host = "rabbitmq-0.rabbitmq.dev"
port = 5672
user = "autorunner"
password = "aaa-@@@-12345"
vhost = "/aaa"


# host = "192.168.99.100"
# port = 30672
# user = "admin"
# password = "admin"
# vhost = "/"

def connect():
    # credentials = pika.PlainCredentials(username=user, password=password)
    # connection = pika.BlockingConnection(pika.ConnectionParameters(
    #     credentials=credentials,
    #     host=host,
    #     port=port,
    #     virtual_host=vhost))
    vhost_t = vhost.replace("/", "%2F")
    password_t = password.replace("@", "%40")
    url = "amqp://%s:%s@%s:%d/%s" % (user, password_t, host, port, vhost_t)
    print(url)
    connection = pika.BlockingConnection(pika.URLParameters(url))
    print(connection)
    return connection


def send():
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    print("Prepare to send")
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
    print("Prepare to recv")
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    send()
    recv()
