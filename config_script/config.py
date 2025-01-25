import json
from strava import StravaClient

#LOAD ENVIRONMENT VARIABLES FOR PROJECT
with open('/workspaces/func-process-webhook-event/local.settings.json','r') as file:
    data = json.load(file)

STRAVA_CLIENT_ID = data['Values']['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET = data['Values']['STRAVA_CLIENT_SECRET']

#CREATE STRAVA CLIENT
myStrava = StravaClient(STRAVA_CLIENT_ID,STRAVA_CLIENT_SECRET)

callback_url = 'https://func-process-webhook-event.azurewebsites.net/api/func_process_webhook_event'
verify_token = '1234'

result = myStrava.create_subscription(callback_url,verify_token)
print(result)

result = myStrava.view_subscriptions()
print(result)

result = myStrava.delete_subscription(272432)
print(result)