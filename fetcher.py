import json
import os
import requests
from os.path import join, isfile
import datetime
from requests_oauthlib import OAuth1, OAuth1Session
from time import sleep

# Ver como manejar esto
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('TR_KEY')
api_secret = os.getenv('TR_SECRET')
token = os.getenv('TR_OATH_TOKEN')
token_secret = os.getenv('TR_OATH_TOKEN_SECRET')
oauth = OAuth1(client_key=api_key, client_secret=api_secret,
                                resource_owner_key=token, resource_owner_secret=token_secret)


def fetch_board_id(board_link):
    http_method = 'GET'
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        http_method,
        f"{board_link}.json",
        headers=headers,
        auth=oauth
    )
    response = response.json()
    return response["id"]


def fetch_board_meta(board_id, target_dir):
    http_method = 'GET'
    headers = {
        "Accept": "application/json"
    }
    url = f"https://api.trello.com/1/boards/{board_id}"
    response = requests.request(
        http_method,
        url,
        headers=headers,
        auth=oauth
    )
    board_info = response.json()
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
        sleep(0.05)
    lists_json = [board_info] + lists_json
    # Probablemente necesita ser manejado globalmente
    fecha = str(datetime.date.today())

    counter = 1
    while isfile(target := join(target_dir, f"{fecha}|{counter}.json")):
        counter += 1

    with open(target, "w") as file:
        json.dump(lists_json, file, indent=2)

if __name__ == "__main__":
    print(fetch_board_id("https://trello.com/b/M4QRcp3l/2021-2"))