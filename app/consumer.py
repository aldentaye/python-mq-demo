import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def consume_messages():
    connection_params = pika.ConnectionParameters(
        host='localhost',                     
        port=5672,                             
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='my_queue')

    print(' [*] Waiting for messages. To exit, press CTRL+C')

    # Set up the callback function for incoming messages
    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

    # Start consuming messages
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(' [*] Stopping consumer...')
        channel.stop_consuming()
        connection.close()

if __name__ == '__main__':
    consume_messages()
