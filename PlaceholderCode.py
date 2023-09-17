#Using twitter api to begin retrieving info from twitter

import tweepy
import os

#Authentication
API_KEY = os.environ.get('api')
API_SECRET_KEY = os.environ.get('secret_key')
ACCESS_TOKEN = os.environ.get('token')
ACCESS_TOKEN_SECRET = os.environ.get('secret_token')

def setup_api():
    """ Setup the tweepy API with authentication. """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api
