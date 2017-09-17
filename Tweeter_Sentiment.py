# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:47:39 2017

@author: piotr_000
"""

from textblob import TextBlob
wiki=TextBlob("Siraj is angry that he never get good matches on Tinder")

print('Tags:')
print(wiki.tags)

print('Words:')
print(wiki.words)

print('Sentiment:')
print(wiki.sentiment.polarity)