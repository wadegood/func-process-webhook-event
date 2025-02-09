Project Overview

This application is desiged to process events generated by the Strava webhook api. Events generated inside of Strava will be pushed to an Azure Function where they can be further processed.

Links

https://developers.strava.com/docs/webhooks/

Prerequisites
1. VSCode with Azure and Dev Container Extension installed 
2. Docker Desktop
3. GIT
4. Azure subscription


Environment Setup
1. Clone the repository to your local machine. Open the repository in VSCode and select "reopen in container". This will create a docker container using the image definition found inside of the .devcontainer directory.
2. Once the container is setup, select the option to create a virtual environment within the container environment.

Configuring Azure Resources
1. Login to Azure using the CLI
  az login
2. Within the terminal, change your directory to config_files
  cd config_files

3. Run the following command to make the azure_resources.sh script executable.
  chmod +x azure_resources.sh

4. Run the script
  ./azure_resources.sh


2. Create a local.settings.json file. The contents of this file should be as shown below. Note you must add an "&" symbol after the strava callback URL value. This is because the azure function URL already contains a parameter appended to the end.

{
    "IsEncrypted": false,
    "Values": {
      "AzureWebJobsStorage": "",
      "FUNCTIONS_WORKER_RUNTIME": "python",
      "STRAVA_CLIENT_ID": "{YOUR_STRAVA_CLIENT_ID}",
      "STRAVA_CLIENT_SECRET": "{YOUR_STRAVA_CLIENT_SECRET}",
      "STRAVA_CALLBACK_URL": "{STRAVA_CALLBACK_URL}&"
  
    }
  }

3. Close and reopen VSCode and a message will appear to create a virtual environment. Select yes to create the virtual python environment inside of your container.


4. Click on run and debug extension on the left hand side. Click the run button. This will start an instance of the function app on your localhost. Once the function app is up an running, copy and paste the URL into a web browser and press enter. You should receive a message stating "Validation Failed. Please try again." This confirms that the function is working as expected and all setup tasks were completed properly. Disconnect the function from the localhost.

Deployment
1. Using the Azure Function extension, click on deploy to Azure.
2. Log in to the Azure Portal and retrieve the function app URL.




5. Under the config file, navigate to the config.ipynb file. Execute the first cell. This will prompt the installation of the kernel package.




