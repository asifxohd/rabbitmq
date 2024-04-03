import pika

def message_received(ch,method, properties, body):
    print(f"received message{body}")

connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=message_received)


print("started consumeing ")
channel.start_consuming() 