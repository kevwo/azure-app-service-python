import os
from sampleapp.common.helpers import set_environmental_variables
set_environmental_variables('config.yml')
from sampleapp.worker import run as worker

if __name__ == '__main__':
    worker.work()