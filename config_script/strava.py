import json
import requests

#LOAD ENVIRONMENT VARIABLES FOR PROJECT
with open('/workspaces/func-process-webhook-event/local.settings.json','r') as file:
    data = json.load(file)

STRAVA_CLIENT_ID = data['Values']['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET = data['Values']['STRAVA_CLIENT_SECRET']

class Strava:

    def __init__(self):
        self.client_id = STRAVA_CLIENT_ID
        self.client_secret = STRAVA_CLIENT_SECRET

    def view_subscriptions(self):
        url = 'https://www.strava.com/api/v3/push_subscriptions'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.get(url=url,params=params)
        return response.content


    def delete_subscription(self, subscription_id):
        url = f'https://www.strava.com/api/v3/push_subscriptions/{subscription_id}'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.delete(url=url,params=params)
        return response.content

    def create_subscription(self, callback_url, verify_token):
        url = 'https://www.strava.com/api/v3/push_subscriptions'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'callback_url': callback_url,
            'verify_token': verify_token
        }
        response = requests.post(url=url,params=params)
        return response.content


myStrava = Strava()

callback_url = 'https://func-process-webhook-event.azurewebsites.net/api/func_process_webhook_event'
verify_token = '1234'


# result = myStrava.create_subscription(callback_url,verify_token)
# print(result)

result = myStrava.view_subscriptions()
print(result)

# result = myStrava.delete_subscription(272386)
# print(result)