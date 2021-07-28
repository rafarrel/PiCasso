"""
    The ProcessTweets class provides tools to process twitter data
    and retrieve images for style_transfer. It retrieves the next streamed tweet,
    processes it to determine if the tweet contains an image (if it doesn't, it
    searches Google Images for an image associated with the text instead),
    downloads the image, and stores it as an Image file to be processed by
    the ProcessImages class.

    Inherits from TwitterInteractor class

    @author Alex Farrell
"""
from PIL import Image
from io import BytesIO
from picasso.twitter.twitterinteractor import TwitterInteractor
from picasso.processing.searchimages import get_image_url
import requests


class ProcessTweets(TwitterInteractor):

    def __init__(self):
        TwitterInteractor.__init__(self)

    def retrieve_next_tweet(self):
        """
            Retrieve the next tweet to be processed from the
            streamed_tweets queue.
        """
        return self.get_streamed_tweets().get()

    def get_queue_size(self):
        """
            Get the size of the streamed tweets queue
            to check if there are more images to process.
        """
        return self.get_streamed_tweets().qsize()

    def process_tweet(self):
        """
            Process the next tweet to determine if it contains an image. If the
            tweet contains an image, download it from Twitter and return it.
            Otherwise, if the tweet only contains text, search Google Images
            for an image associated with the text and return that.
        """
        next_tweet = self.retrieve_next_tweet()
        for media in next_tweet.entities.get("media", [{}]):
            if media.get("type", None) == "photo":
                return self.get_image(media)
            else:
                return self.search_image(next_tweet.text)

    def get_image(self, media):
        """
            Download the image from a tweet and return it as an Image
            object.
        """
        response = requests.get(media["media_url"])
        return Image.open(BytesIO(response.content))

    def search_image(self, text_input):
        """
            Search Google Images for an image associated with a string of
            text.
        """
        response = requests.get(get_image_url(text_input))
        return Image.open(BytesIO(response.content))

