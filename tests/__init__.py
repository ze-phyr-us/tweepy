"""
Testing credentials
"""

from tweepy.client import Client
from tweepy.auth import OAuth
from tweepy.oauth2 import Consumer, Token

consumer = Consumer('key', 'secret')
access_token = Token('key', 'secret')

def create_test_client():
    return Client(auth=(OAuth, consumer, access_token))

