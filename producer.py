import pika 

connection_params = pika.ConnectionParameters(
    host='localhost',  # Change this if your RabbitMQ server is on a different host
    port=15672,          # Default RabbitMQ port
    protocol=pika.spec.PUBLISHER_CONFIRM_PROTOCOL,
    credentials=pika.PlainCredentials('user', 'SDnUEeh00Ulrl0Gl'),
)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='my_queue')

message = "Hello, Message Queue"

channel.basic_publish(exchange='',
                      routing_key='my_queue',
                      body=message)

print(f" [x] Sent '{message}'")

connection.close()