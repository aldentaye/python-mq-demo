import pika 

connection_params = pika.ConnectionParameters(
        host='localhost',                     
        port=5672,                             
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