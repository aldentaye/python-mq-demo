import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

connection_params = pika.ConnectionParameters(
    host='localhost',
    port=15672,
    credentials=pika.PlainCredentials('user', 'SDnUEeh00Ulrl0Gl'),
)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='my_queue')

channel.basic_consume(queue='my_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
