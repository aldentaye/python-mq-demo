from flask import Flask, render_template, redirect, url_for
import pika

app = Flask(__name__)

# RabbitMQ Connection Parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'message_queue'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message')
def send_message():
    try:
        # Connect to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue=RABBITMQ_QUEUE)

        # Send a message to the queue
        message = 'Hello, RabbitMQ!'
        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)

        # Close the connection
        connection.close()

    except Exception as e:
        return f"Error: {str(e)}"

    return redirect(url_for('home'))

@app.route('/release_message')
def release_message():
    try:
        # Connect to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue=RABBITMQ_QUEUE)

        # Consume and release a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE)

        if method_frame:
            print(f"Received message: {body.decode('utf-8')}")
            # Acknowledge the message (release)
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)

        # Close the connection
        connection.close()

    except Exception as e:
        return f"Error: {str(e)}"

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)