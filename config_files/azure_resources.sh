# Function app and storage account names must be unique.

# Variable block
let "randomIdentifier=$RANDOM*$RANDOM"
location="westus"
resourceGroup="rg-strava-$randomIdentifier"
tag="create-function-app-consumption"
storage="dlsstravaevents$randomIdentifier"
functionApp="func-process-webhook-event-$randomIdentifier"
skuStorage="Standard_LRS"
functionsVersion="4"
runtime="python"
runtimeVersion="3.11"
os="linux"

# Create a resource group
echo "Creating $resourceGroup in "$location"..."
az group create --name $resourceGroup --location "$location" --tags $tag

# Create an Azure storage account in the resource group.
echo "Creating $storage"
az storage account create --name $storage --location "$location" --resource-group $resourceGroup --sku $skuStorage

# Create a serverless function app in the resource group.
echo "Creating $functionApp"
az functionapp create --name $functionApp --storage-account $storage --consumption-plan-location "$location" --resource-group $resourceGroup --functions-version $functionsVersion --runtime $runtime --os-type $os --runtime-version $runtimeVersion