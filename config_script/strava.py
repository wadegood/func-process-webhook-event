import json
import requests

class StravaClient:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

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