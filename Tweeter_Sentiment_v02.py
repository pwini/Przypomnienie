# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:00:46 2017

@author: piotr_000
"""

import tweepy
from textblob import TextBlob

consumer_key = '5Sw1EvVuuM5zzanS6NwYoeJb7'
consumer_secret = 'P39t3POzKkGVqyqlCsnuW21qgTazr2Co1eeYkI4uwdFsUhdqvW'

access_token = '909414255404961792-MJATezDW4WuqxcIq7Q6rO7ftVqDaMHh'
access_token_secret = 'WIEDpHNTgtG7Y4MpxR7Cu62NLnY5D335k8Nu6XpsLnbe8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('HSBC')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)