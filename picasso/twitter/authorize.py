"""
    Use the given credentials to authorize the use of the Twitter APIs for
    PiCasso and retrieve an object to allow it to access them.

    @author Alex Farrell
"""

import picasso.twitter.credentials as creds
import tweepy


authorize = tweepy.OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
authorize.set_access_token(creds.ACCESS_KEY, creds.ACCESS_SECRET)
api_access = tweepy.API(authorize)