"""
    Runs PiCasso's selected interface, allowing the user to interact with
    the robot.

    Execution example:
                            python3 picasso     [If in PiCasso directory]
                            python3 main.py     [If in Picasso/picasso directory]

    NOTICE: As of right now, when running in the terminal, a virtual environment
    is required or we have to specifically state the path to the PiCasso/picasso
    directory in GLOBALPATH in order for the packages to be recognized

    PACKAGING: After we have given PiCasso full functionality and have a
    working prototype, we can use python's setup tools to package
    the project for exporting. This will make it easier to run on the Pi
    so we can implement this for our presentations in CS 121 and the CS Fair.
    This should be done after we have completed testing and have a solid
    prototype. If we decide to add more features after packaging, we can repackage
    the project and update it on the pi.

    @author Alex Farrell
"""
from picasso.interfaces.commandline import execute
from picasso.interfaces.commandline import display_goodbye_message

if __name__ == '__main__':
    try:
        execute()
    except KeyboardInterrupt:
        display_goodbye_message()