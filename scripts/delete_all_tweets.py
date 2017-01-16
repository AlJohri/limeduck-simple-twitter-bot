#!/usr/bin/env python3

import os, logging

from blessings import Terminal
t = Terminal()

import tweepy
from os import path
from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), os.path.pardir, '.env')
load_dotenv(dotenv_path)

auth = tweepy.OAuthHandler(
    os.environ['TWITTER_CONSUMER_KEY'],
    os.environ['TWITTER_CONSUMER_SECRET'])

auth.set_access_token(
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_SECRET'])
api = tweepy.API(auth)

for i, status in enumerate(tweepy.Cursor(api.user_timeline).items()):
    try:
        api.destroy_status(status.id)
        print(i, "Deleted:", status.id)
    except Exception as e:
        print(i, t.red(str(e)))
        print("Failed to delete: " + str(status.id))
