# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:53:33 2017

@author: Finne
"""

import tweepy

def Tweet(wxFile):
    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = '' #keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = ''#keep the quotes, replace this with your access token
    ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
     
    filename=open(wxFile,'r')
    f=filename.readlines()
    filename.close()
     
    for line in f:
        api.update_status(line)
    #    time.sleep(900)#Tweet every 15 minutes