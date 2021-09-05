import json
import os
from requests_oauthlib import OAuth1Session


expiration = 'never'
scope = 'read,write,account'
key = None
secret = None
name = 'Softnahoria'

token_req_url = 'https://trello.com/1/OAuthGetRequestToken'
auth_url = 'https://trello.com/1/OAuthAuthorizeToken'
token_access_url = 'https://trello.com/1/OAuthGetAccessToken'

# Código basado en py-trello
# [https://github.com/sarumont/py-trello/]


def token_creator():
    session = OAuth1Session(client_key=os.getenv('TR_KEY'), client_secret=os.getenv('TR_SECRET'))
    response = session.fetch_request_token(token_req_url)
    resource_owner_key, resource_owner_secret = response.get('oauth_token'), response.get('oauth_token_secret')

    print("Token temporal creado:")
    print("    - oauth_token        = %s" % resource_owner_key)
    print("    - oauth_token_secret = %s" % resource_owner_secret)
    print("")

    print("Para continuar, porfavor ingresa al siguiente link...")
    print(f'{auth_url}?oauth_token={resource_owner_key}&scope={scope}&expiration={expiration}&name={name}')
    oauth_verifier = input('Porfavor ingresa el código de autorización')
    session = OAuth1Session(client_key=os.getenv('TR_KEY'), client_secret=os.getenv('TR_SECRET'),
                            resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret,
                            verifier=oauth_verifier)
    access_token = session.fetch_access_token(token_access_url)
    print("Access Token:")
    print("    - oauth_token        = %s" % access_token['oauth_token'])
    print("    - oauth_token_secret = %s" % access_token['oauth_token_secret'])
    print("")
    print("Puedes utilizar estos datos para autorizar")
    print("* Los datos fueron guardados en secret.json. Recuerda editar el archivo .env")
    yeison = {
        'OATH_TOKEN': access_token['oauth_token'],
        'OATH_TOKEN_SECRET': access_token['oauth_token_secret']
    }
    with open('secret.json', 'w') as file:
        json.dump(yeison, file)

token_creator()