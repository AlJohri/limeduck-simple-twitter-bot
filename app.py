#!/usr/bin/env python3

import os
import sys
import tweepy
import logging
from os import path
from dotenv import load_dotenv

from blessings import Terminal
t = Terminal()

# logging.basicConfig(level=logging.DEBUG, format='[%(name)s] %(asctime)s %(message)s')

from utils import remove_extra_spaces, tweet_generator

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

with open("mobydick.txt") as f:
    source_text = remove_extra_spaces(f.read())

gen = tweet_generator(source_text)
gen.send(None)

screen_names = [
    'aljohri',
    'nytimes',
    'washingtonpost',
    'fivethirtyeight',
    'coreyspring',
    'ABC',
    'WLOX',
    'WestWingReport',
    'Slate',
    'TechCrunch',
    'WSJ',
    'CNN',
    'paulapoundstone',
    'BBCWorld',
    'WLBT',
    'hardwick',
    'realDonaldTrump',
]

# for username in itertools.cycle(twitter_handles):
#     
#     text = f"@{username} {tweet}"
#     print(text)

auth = tweepy.OAuthHandler(
    os.environ['TWITTER_CONSUMER_KEY'],
    os.environ['TWITTER_CONSUMER_SECRET'])

auth.set_access_token(
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_SECRET'])

api = tweepy.API(auth)

# https://dev.twitter.com/streaming/overview/request-parameters#follow

class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420: # exceeded number of requests to connect to streaming api within window of time
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, status):
        user = status.user

        if user.id not in user_ids:
            # print(f"Skipping tweet by @{user.screen_name}... not in list.")
            return

        username = user.screen_name
        tweet = gen.send(username)
        text = f".@{username} {tweet}"
        print(f"In response to @{user.screen_name} "
              f"tweeting with length {len(text)}: {text}", end="...")

        try:
            api.update_status(text) # in_reply_to_status_id=status.id
            print("success")
        except tweepy.error.TweepError as e:
            print("error")
            print(t.red(str(e)))

users = api.lookup_users(screen_names=screen_names)
user_ids = [u.id for u in users]

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

user_names = ", ".join(f"{user.screen_name}" for user in users)
print(f"Following: {user_names}\n")
myStream.filter(follow=[str(x) for x in user_ids])
# retweeted_status