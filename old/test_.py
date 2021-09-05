import requests
from requests_oauthlib import OAuth1, OAuth1Session
from dotenv import load_dotenv
import os
import json
from os import environ
import pprint

load_dotenv()

api_key = os.getenv('TR_KEY')
api_secret = os.getenv('TR_SECRET')
token = os.getenv('TR_OATH_TOKEN')
token_secret = os.getenv('TR_OATH_TOKEN_SECRET')

oauth = OAuth1(client_key=api_key, client_secret=api_secret,
                                resource_owner_key=token, resource_owner_secret=token_secret)

http_method = 'GET'

headers = {
   "Accept": "application/json"
}

board_id = "612136c374b1e9895ce3c6c4"
board_id = "61343901eb5d4920348e9b47"

url = f"https://api.trello.com/1/boards/{board_id}"
response = requests.request(
    http_method,
    url,
    headers=headers,
    auth=oauth
)
response = response.json()
board_info = response

url = f"https://api.trello.com/1/boards/{board_id}/lists"
response = requests.request(
    http_method,
    url,
    headers=headers,
    auth=oauth
)
lists_json = response.json()
for list_ in lists_json:
    url = f"https://api.trello.com/1/lists/{list_['id']}/cards"
    response = requests.request(
        http_method,
        url,
        headers=headers,
        auth=oauth
    )
    list_['cards'] = response.json()
lists_json = [board_info] + lists_json
out_file = open("../test_board.json", "w")
json.dump(lists_json, out_file, indent=2)
out_file.close()



