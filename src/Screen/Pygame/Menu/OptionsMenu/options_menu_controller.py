from Screen.Pygame.Controller.controller import Controller
from InputProcessor import commands

from Menu.OptionsMenu.options_menu import OptionsMenu
from Screen.Pygame.Menu.OptionsMenu.options_menu_screen import OptionsMenuScreen


class OptionsMenuController(Controller):
    """ Controller for the options menu """
    
    def __init__(self):
        """ Builds the Options Menu Controller """
        Controller.__init__(self)
        self.menu = OptionsMenu()
        self.screen = OptionsMenuScreen(self.menu)
        self.cmds = {commands.EXIT:self.stopRunning}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running