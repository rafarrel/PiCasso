"""
    The TransferStyles class retrieves an image from the ProcessTweets class,
    runs a style transfer on it using a selected, pre-trained style model,
    and passes the result to the ProcessImages class.

    Inherits from ProcessTweets class

    @author Alex Farrell
"""
from picasso.processing.processtweets import ProcessTweets
from picasso.art_generation.style_transfer.transfer import transfer


class TransferStyles(ProcessTweets):

    def __init__(self):
        ProcessTweets.__init__(self)
        self.next_image = None
        self.next_style_model = None
        self.next_image_data = None

    def prepare_image_for_transfer(self):
        """
            Retrieve the next image from the Twitter Stream to
            prepare for style transfer.
        """
        self.next_image = self.process_tweet()

    def select_style(self, style_model_path):
        """
            Select the pre-trained style model to be used
            for style transfer
        """
        self.next_style_model = style_model_path

    def conduct_transfer(self):
        """
            Transfer the style from the selected pre-trained
            style model to the image retrieved from the Twitter
            stream
        """
        self.next_image = transfer(self.next_image, self.next_style_model)
        #self.styled_image.show()

    def transfer_style(self):
        """
            Complete style transfer of the content image. Compiles all methods together
            for simplicity.
        """
        self.prepare_image_for_transfer()
        self.conduct_transfer()
        return self.next_image
