from flask import Flask, render_template, redirect, url_for, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import pika

app = Flask(__name__)

# RabbitMQ Connection Parameters
RABBITMQ_HOST = 'flask-app-flask-chart-rabbitmq-service'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'message_queue'

requests_total = Counter('app_requests_total', 'Total number of requests')
request_duration = Histogram('app_request_duration_seconds', 'Request duration in seconds')

def check_rabbitmq_connection():
    try:
        connection = pika.BlockingConnection(rpika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        connection.close()
        return True
    except Exception as e:
        print(f"Error connecting to RabbitMQ: {e}")
        return False


@app.route('/')
def home():
    rabbitmq_status = "Connected" if check_rabbitmq_connection() else "Not Connected"
    requests_total.inc()
    # Record the duration of the request
    with request_duration.time():
        return render_template('index.html', rabbitmq_status=rabbitmq_status)


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    message = request.form['message']
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()
        # declare the queue
        channel.queue_declare(queue=RABBITMQ_QUEUE)

        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)

        connection.close()

    except Exception as e:
        return f"Error: {str(e)}"

    return redirect(url_for('home'))


# @app.route('/release_message')
# def release_message():
#     try:
#         # Connect to RabbitMQ
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
#         channel = connection.channel()

#         # Declare the queue
#         channel.queue_declare(queue=RABBITMQ_QUEUE)

#         # Consume and release a message from the queue
#         method_frame, header_frame, body = channel.basic_get(queue=RABBITMQ_QUEUE)

#         if method_frame:
#             print(f"Received message: {body.decode('utf-8')}")
#             # Acknowledge the message (release)
#             channel.basic_ack(delivery_tag=method_frame.delivery_tag)

#         # Close the connection
#         connection.close()

#     except Exception as e:
#         return f"Error: {str(e)}"

#     return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)