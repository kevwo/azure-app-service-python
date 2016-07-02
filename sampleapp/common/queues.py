import os
import azure.servicebus


class ServiceBusQueue:
    def __init__(self, queue_name):
        self.bus_service = azure.servicebus.ServiceBusService(service_namespace=os.environ["SERVICE_BUS_NAMESPACE"],
                                                              shared_access_key_name=os.environ["SERVICE_BUS_QUEUE_ACCESS_KEY_NAME"],
                                                              shared_access_key_value=os.environ["SERVICE_BUS_QUEUE_ACCESS_KEY_VALUE"])
        self.queue_name = queue_name

    def enqueue(self, job):
        self.bus_service.send_queue_message(self.queue_name, job)

    def dequeue(self):
        """
        Make sure to delete the job with job.delete() after processing
        """
        job = self.bus_service.receive_queue_message(self.queue_name, peek_lock=True)
        return job
