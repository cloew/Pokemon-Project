from Controller.controller import Controller
from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor

from Menu.OptionsMenu.options_menu import OptionsMenu
from Screen.Console.OptionsMenu.options_menu_screen import OptionsMenuScreen


class OptionsMenuController(Controller):
    """ Controller for the options menu """
    
    def __init__(self):
        """ Builds the Options Menu Controller """
        self.menu = OptionsMenu()
        self.screen = OptionsMenuScreen(self.menu)
        self.cmds = {commands.EXIT:self.menu.quit}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running