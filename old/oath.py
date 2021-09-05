import requests
from requests_oauthlib import OAuth1, OAuth1Session
from dotenv import load_dotenv
import os
from os import environ

load_dotenv()


session = OAuth1Session(client_key=os.getenv('TR_KEY'), client_secret=os.getenv('TR_SECRET'))
response = session.fetch_request_token('https://trello.com/1/OAuthGetRequestToken')
resource_owner_key, resource_owner_secret = response.get('oauth_token'), response.get('oauth_token_secret')

print("Request Token:")
print("    - oauth_token        = %s" % resource_owner_key)
print("    - oauth_token_secret = %s" % resource_owner_secret)
print("")

print(f'https://trello.com/1/OAuthAuthorizeToken?oauth_token={resource_owner_key}&scope=read,write,account&expiration=never&name=softnahoria')

oauth_verifier = input(' enter')

session = OAuth1Session(client_key=os.getenv('TR_KEY'), client_secret=os.getenv('TR_SECRET'),
                            resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret,
                            verifier=oauth_verifier)
access_token = session.fetch_access_token('https://trello.com/1/OAuthGetAccessToken')
print("Access Token:")
print("    - oauth_token        = %s" % access_token['oauth_token'])
print("    - oauth_token_secret = %s" % access_token['oauth_token_secret'])
print("")
print("You may now access protected resources using the access tokens above.")
print("")
