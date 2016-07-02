## Basic App Setup
1. Create a Resource Group in Azure RM
2. Create App Service WebApp
 * Set the Python Version in application settings to 3.4
3. Create WebJob for worker
 * Select the continuous WebJob option
4. Take the WebJob name for #2, and put this in bot/__init__.py as name
 * This is used to deploy the WebJob later on
 * Upload a dummy file for now. (It must have a .exe, .py, etc. extension to upload)
5. Create deployment credentials and configure App Service for local git deployment. Add this as a remote to your local git repo. Name this remote azure
6. git push azure master

## Advanced Resources
1. Create Service Bus Namespace - https://azure.microsoft.com/en-us/documentation/articles/service-bus-python-how-to-use-queues/
2. Create Service Bus Queue under the namespace
 * Check Lock Duration timer and make sure it is 30 seconds
 * Create a shared access policy named "worker" with properties send and listen
 * Make sure to update tartest/queues.py with NAMESPACE
3. Store these keys in the App Service WebApp Application Settings with the following App Settings key: JOBS_WORKER