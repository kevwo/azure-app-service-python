import os
from sampleapp.common.helpers import set_environmental_variables
set_environmental_variables('config.yml')
from sampleapp.server import app

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', 80))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT)