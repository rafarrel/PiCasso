"""
    The ProcessImages class provides tools to prepare retrieved images for
    drawing. It is used to receive the next styled image, get
    the data from the image, loop through all pixels in the image and store the
    RGBA values in a list indexed by the each pixel's coordinates. The processed
    list can then be retrieved by the Drawing class and drawn.

    Inherits from TransferStyles.

    @author Alex Farrell
"""
from picasso.processing.transferstyles import TransferStyles


class ProcessImages(TransferStyles):

    def __init__(self):
        TransferStyles.__init__(self)
        self.styled_image = None
        self.styled_image_data = None
        self.image_width = None
        self.image_height = None
        self.processed_image = []

    def retrieve_styled_image(self):
        """
            Retrieve the styled image to process from the TransferStyles class
            and its data.
        """
        self.styled_image = self.transfer_style()
        self.styled_image_data = self.styled_image.load()

    def retrieve_image_size(self):
        """
            Retrieve the width and height of the next image to process.
        """
        self.image_width, self.image_height = self.styled_image.size

    def store_image_rgba_values(self):
        """
            Store the image's RGBA values in a two-dimensional list indexed
            by each pixel's coordinates.

            Example indexing:
                                self.processed_image[50, 65]

            -returns a tuple containing the RGBA values of the
            pixel with coordinates of (50, 65) in the image
        """
        self.processed_image = [[self.styled_image_data[x, y] for y in range(self.image_height)]
                                for x in range(self.image_width)]

    def process_image(self):
        """
            Complete processing of the image to prepare for style_transfer. Compiles
            all processing methods together into one method for simplicity.
        """
        self.retrieve_styled_image()
        self.retrieve_image_size()
        self.store_image_rgba_values()
        return self.processed_image




