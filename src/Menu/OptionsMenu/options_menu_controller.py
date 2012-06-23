from Controller.controller import Controller
from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.GUI.screen import screen

from Menu.OptionsMenu.options_menu import OptionsMenu
from Screen.GUI.OptionsMenu.options_menu_view import OptionsMenuScreen


class OptionsMenuController(Controller):
    """ Controller for the options menu """
    
    def __init__(self):
        """ Builds the Options Menu Controller """
        self.menu = OptionsMenu()
        self.optionsScreen = OptionsMenuScreen(self.menu)
        self.cmds = {commands.EXIT:self.menu.quit}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.optionsScreen
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running