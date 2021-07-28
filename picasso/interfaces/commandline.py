"""
    Commandline interface for PiCasso. Allows users to interact with and
    control the robot. Users are given a menu of options to choose from
    and their selection determines what PiCasso does next.

    @author Alex Farrell
"""
from picasso.interfaces.commandlineengine import CommandLineEngine


def execute():
    """
        Execute commandline interface for PiCasso. Called in __main__.py
        when commandline interface is being used.
    """
    cmd = CommandLineEngine()
    cmd.display_welcome_message()
    while cmd.still_running():
        cmd.run_menu()


def display_goodbye_message():
    """
        Bids the user farewell in the most chivalrous way possible when they
        decide to quit.
    """
    print("\n\nSee ya later :)")








