"""
    The CommandLineEngine class provides functionality for the commandline
    interface and acts as a glue between PiCassoController and the
    interface.

    It inherits from the PiCassoController class.

    @author Alex Farrell
"""
from picasso.control.picassocontroller import PiCassoController
import picasso.interfaces.options as options
import picasso.control.possible_selections as ps
import picasso.art_generation.style_transfer.engine.style_transfer_model_paths as mp

class CommandLineEngine(PiCassoController):


    def __init__(self):
        PiCassoController.__init__(self)
        self.user_input = None
        self.has_not_quit = True

    def run_menu(self):
        """
            Display menu and get the desired choice from the user. Then
            perform the appropriate action based on the selected choice.
        """
        self.display_menu()
        self.get_user_choice()
        self.process_user_choice()

    def display_welcome_message(self):
        """
            Display welcome message to the user.
        """
        print("Ello matey! Welcome to PiCasso, the totally epic\n"
              "style_transfer robot created by Alex \'Noobik\'s Cube\' Farrell,\n"
              "Cam \'Skate God\' Hudson, and Drew \'Theeeee RA\' Meyers!\n")

    def display_menu(self):

        """
            Display the menu of choices to the user.
        """
        print("-----------------------\n"
              "Options:\n\n"
              "(S) Start new Twitter stream\n"
              "(E) End current Twitter stream\n"
              "(W) Write styled image to file\n" 
              "(D) Draw next image\n"
              "(Q) Quit\n"
              "-----------------------\n")

    def display_error_message(self):
        """
            Display error message when user picks an
            invalid choice.
        """
        print('Invalid choice. Try another...\n')

    def get_user_choice(self):
        """
            Get menu choice selected by the user.
        """
        self.user_input = input('Select ya option: ').upper()

    def process_user_choice(self):
        """
            Process the option selected by the user and decide
            what PiCasso should do.
        """
        if self.user_input == options.START_STREAM:
            self.start_stream()                        # from TwitterInteractor
        elif self.user_input == options.END_STREAM:
            self.end_stream()                          # from TwitterInteractor
        elif self.user_input == options.WRITE:
            self.write_image_to_file()
        elif self.user_input == options.DRAW:
            print(self.get_styled_image_data_to_draw())  # from PiCassoController
        elif self.user_input == options.QUIT:
            self.quit()
        else:
            self.display_error_message()

    def still_running(self):
        """
            Return the current state of user selection (True if the user
            is still accessing the menu and False if the user has chosen
            to quit).
        """
        return self.has_not_quit

    def quit(self):
        """
            Prepare for quitting the commandline menu.
        """
        self.end_stream()
        self.has_not_quit = False

    def display_style_choices(self):
        """
            Display the style choices the user can
            select.
        """
        print("\n1) La Muse\n" +
                "2) Rain Princess\n" +
                "3) Shipwreck\n" +
                "4) The Scream\n" +
                "5) Udnie\n" +
                "6) Wave\n")

    def get_style_choice(self):
        """
            Select the style to be used for next style
            transfer
        """
        self.display_style_choices()
        self.style_input = input('Enter style choice:')
        if self.style_input == ps.LA_MUSE:
            self.select_style(mp.LA_MUSE)
        elif self.style_input == ps.RAIN_PRINCESS:
            self.select_style(mp.RAIN_PRINCESS)
        elif self.style_input == ps.SHIPWRECK:
            self.select_style(mp.SHIPWRECK)
        elif self.style_input == ps.THE_SCREAM:
            self.select_style(mp.THE_SCREAM)
        elif self.style_input == ps.UDNIE:
            self.select_style(mp.UDNIE)
        elif self.style_input == ps.WAVE:
            self.select_style(mp.WAVE)
        else:
            print('Invalid selection.\n')