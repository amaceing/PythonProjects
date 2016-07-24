import sys
sys.path.insert(0, '/requests/requests')

import requests
import config
import json

auth_API_call = 'https://www.reddit.com/api/v1/authorize?'
client_id = 'client_id' + config.credentials['client_id']
user_agent = {'user_agent': 'mace:pythonprojecsredditAPI:v1.0 (by /u/codeycoderson)'}
redirect_uri = config.credentials['redirect_uri']
scope = 'identity'

response = requests.get(r'http://www.reddit.com/user/codeycoderson/comments/.json', headers = user_agent)
responseData = response.json()

print(responseData)
