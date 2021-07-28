"""
    The PiCassoController class collects all functional parts of Picasso
    into one space and acts as the brain of the robot. Everything can be
    controlled from this class.

    It inherits from ProcessImages class.
    @author Alex Farrell
"""
from picasso.processing.processimages import ProcessImages
#from picasso.drawing.PiCassoBody import PiCasso
import picasso.art_generation.style_transfer.engine.style_transfer_model_paths as mp


class PiCassoController(ProcessImages):

    def __init__(self):
        ProcessImages.__init__(self)
        #PiCasso.__init__(self)
        self.style_input = None
        self.next_style_model = mp.SHIPWRECK



    def get_styled_image_data_to_draw(self):
        """
             Get the coordinates and rgba values of the styled
             image to draw.
        """
        if self.get_queue_size() > 0:
            self.get_style_choice()         # Must be defined by interface
            return self.process_image()     # that inherits the controller
        else:
            print('\nNo image to process...')
            return None

    def get_image_path(self):
        """
            Get path of image to write
        """
        output_path = input("\nEnter image name to be stored:")
        return mp.IMAGE_PATH + output_path
        #print(output_path)

    def write_image_to_file(self):
        """
            Optional method to write the styled image to an
            output file
        """
        if self.get_queue_size() > 0:
            self.get_style_choice()         # Must be defined by interface
            self.process_image()            # that inherits the controller
            self.styled_image.save(self.get_image_path())
        else:
            print('\nNo image to process.')






