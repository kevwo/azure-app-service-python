import os
import sys
if os.environ.get('LOCAL', False) != "True":
    sys.path.append(os.environ['WEBROOT_PATH'])  # access my app libraries
    sys.path.append(os.path.join(os.environ['WEBROOT_PATH'], "env", "Lib", "site-packages"))  # access requirements.txt

import time

from sampleapp.common.queues import ServiceBusQueue

Queue = ServiceBusQueue(os.environ['SERVICE_BUS_QUEUE_NAME'])


def work():
    while True:
        job = Queue.dequeue()
        if job.location is None:
            print("sleep-5")
            sys.stdout.flush()
            time.sleep(5)
        else:
            print(job.body.decode("utf-8"))
            sys.stdout.flush()
            job.delete()

if __name__ == "__main__":
    work()