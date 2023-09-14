#Using twitter api to begin retrieving info from twitter

import tweepy
import os

#Authentication
API_KEY = os.environ.get('api')
API_SECRET_KEY = os.environ.get('secret_key')
ACCESS_TOKEN = os.environ.get('token')
ACCESS_TOKEN_SECRET = os.environ.get('secret_token')