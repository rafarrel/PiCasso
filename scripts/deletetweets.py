"""
    Script to delete all tweets from PiCasso's Twitter Account

    @author Alex Farrell
"""
from picasso.twitter.authorize import api_access
import tweepy

try:
    for status in tweepy.Cursor(api_access.user_timeline).items():
        api_access.destroy_status(status.id)
        print("Deleting: " + str(status.id))
except:
    print("ERROR: Deleting tweets failed.")
finally:
    print("\nDone.")
