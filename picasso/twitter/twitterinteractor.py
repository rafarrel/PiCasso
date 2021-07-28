"""
    The TwitterInteractor class provides interaction with PiCasso's twitter
    account. It provides methods for retrieving tweets, streaming tweets, etc.
    It stores all streamed tweets in a Queue that is then passed onto the
    ProcessTweets class.

    @author Alex Farrell
"""
from picasso.twitter.credentials import PICASSO_USERNAME
from picasso.twitter.authorize import api_access
from picasso.twitter.credentials import TWITTER_ID
from queue import Queue
import tweepy


class TwitterInteractor:

    def __init__(self):
        self.USERNAME = PICASSO_USERNAME
        self.stream_listener = self.TwitterInteractorStreamListener()
        self.api = api_access
        self.user_stream = None
        self.is_streaming = False

    def retrieve_tweet(self, tweet_num):
        """
            Retrieve a specific tweet from PiCasso's timeline.
        """
        try:
            return self.api.user_timeline(username=self.USERNAME)[tweet_num]
        except IndexError:
            print("Tweet at that index doesn't exist. Use a lower number.")

    def tweet_out_image(self, filepath, tweet_message):
        """
            Tweet out drawn images to PiCasso's Twitter account
        """
        self.api.update_with_media(filepath, tweet_message)

    def create_stream(self):
        """
            Create a stream object to be used for real-time retrieval
            of tweets from PiCasso's Twitter account.
        """
        self.user_stream = tweepy.Stream(auth=self.api.auth, listener=self.stream_listener)

    def start_stream(self):
        """
            Start the stream for real-time retrieval of tweets from
            PiCasso's Twitter account.
        """
        # Only start stream if there isn't already one going
        if not self.is_streaming:
            try:
                self.create_stream()
                self.user_stream.filter(follow=[TWITTER_ID], is_async=True)
                self.is_streaming = True
            except tweepy.error.TweepError:
                print("Connection was broken.")
            except:
                print("Cannot connect to stream.")
        else:
            print("\nAlready streaming...\n")


    def end_stream(self):
        """
            End the stream for real-time retrieval of tweets from
            PiCasso's Twitter account.
        """
        try:
            self.is_streaming = False
            self.user_stream.disconnect()
            del self.user_stream
        except AttributeError:
            pass

    def get_streamed_tweets(self):
        """
            Return the queue of streamed tweets
        """
        return self.stream_listener.streamed_tweets


    class TwitterInteractorStreamListener(tweepy.StreamListener):
        """
            Twitter stream object for real-time data retrieval from twitter
            for the TwitterInteractor class.
        """
        INFINITE = 0

        def __init__(self):
            self.api = api_access
            self.streamed_tweets = Queue(maxsize=self.INFINITE)

        def on_status(self, status):
            """
                Override the StreamListener class's on_status method to display
                streamed tweet text to the console and add streamed tweets
                to the queue for processing
            """
            self.streamed_tweets.put(status)
            print(status.text)


