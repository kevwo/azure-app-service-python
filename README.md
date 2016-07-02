# azure-app-service-python
Sample WebApp and WebJob in python hosted via Azure App Service.

This consists of a Flask App that will place jobs in an Azure Service Bus Queue along with a Worker (WebJob) that processes items on the Service Bus Queue.

## Basic App Setup
1. Create a `config.yml` file in the project root - next to `deploy.cmd`.
 * A full example file can be found at the bottom of this readme
2. Create Service Bus Namespace
 * Put the name in `config.yml` under key `SERVICE_BUS_NAMESPACE`
3. Create Service Bus Queue under the namespace
 * Put the queue name in `config.yml` under `SERVICE_BUS_QUEUE_NAME`
 * Check Lock Duration timer and make sure it is 30 seconds
 * Create a shared access policy named with properties send and listen
  * Put the shared accesskey name & shared accesskey value in `config.yml` under `SERVICE_BUS_QUEUE_ACCESS_KEY_NAME`, `SERVICE_BUS_QUEUE_ACCESS_KEY_VALUE`
4. Finish preparing the `config.yml` with a few basic values:
 * `LOCAL: True`
 * `SERVER_HOST: "localhost"`
 * `SERVER_PORT: 80`

## Running locally
1. To start the server, navigate to the project root and run `python runserver.py`
 * Open your webrowser and go to `http://localhost` You should see Hello, World!
 * Neviaget to `http://localhost/test` You should see a message being enqueued with the current timestamp.
2. To start the worker, navigate to the project root and run `python runworker.py`
 * You should see a console trace immediately processing the message you previously sent

## Hosting on Azure App Service
1. Create a Resource Group in Azure RM
2. Create App Service WebApp
 * Set the Python Version in Settings -> Application Settings to 3.4
3. Create WebJob for worker (under Settings -> WebJobs)
 * Select the continuous WebJob option
 * Upload a dummy file for now. (It must have a .exe, .py, etc. extension to upload)
 * Take the WebJob name, and put this in `sampleapp.worker/__init__.py` as `name = 'WHATEVER_NAME_YOU_CHOSE'`
4. Set environmental variables (from `config.yml`) in Settings -> Application Settings under app settings.
 * Copy Key and Values from `config.yml` precisely. (Leave out `LOCAL: True` from Azure though)
 * Don't use quotations when pasting values in Azure App Settings.
5. Create deployment credentials (under Settings -> Publishing)
6. Go to Deployment source and chose the source Local Git Repository
7. Add this as a remote to your local git repo. Name this remote azure
 * `git remote add azure https://username@needsmoregit.scm.azurewebsites.net:443/NeedsMoreGit.git`
8. Deploy via `git push azure master`

## Customizations
* If you rename the "sampleapp" python package, or the server/worker packages, you need to make the following changes.
 * Replace all package imports with the new name. Don't forget to also replace
 * deploy_job.py
 * runserver.py
 * runworker.py
 * web.config: <add key="WSGI_ALT_VIRTUALENV_HANDLER" value="sampleapp.server.app" />
* You should not modify ptvs_virtualenv_proxy.py

## Sample config.yml
```
LOCAL: True
SERVICE_BUS_NAMESPACE: "samplenamespace"
SERVICE_BUS_QUEUE_NAME: "sampleapp"
SERVICE_BUS_QUEUE_ACCESS_KEY_NAME: "worker"
SERVICE_BUS_QUEUE_ACCESS_KEY_VALUE: "aCVh23a*********************************tys="
SERVER_HOST: "localhost"
SERVER_PORT: 80
```
