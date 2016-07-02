import os
import datetime
from flask import Flask
from azure.servicebus import Message
from sampleapp.common.queues import ServiceBusQueue


Queue = ServiceBusQueue(os.environ['SERVICE_BUS_QUEUE_NAME'])
app = Flask(__name__, static_folder='../static')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def test():
    try:
        current_time = str(datetime.datetime.now())
        job = Message(bytes('Dummy Message at ' + str(current_time), 'utf-8'))
        Queue.enqueue(job)
        return 'Enqueued message: ' + job.body.decode("utf-8")
    except Exception as e:
        print(e)
        raise
