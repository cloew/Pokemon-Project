from InputProcessor import commands

from kao_gui.pygame.pygame_controller import PygameController

from Menu.OptionsMenu.options_menu import OptionsMenu
from Screen.Pygame.Menu.OptionsMenu.options_menu_screen import OptionsMenuScreen


class OptionsMenuController(PygameController):
    """ Controller for the options menu """
    
    def __init__(self):
        """ Builds the Options Menu Controller """
        self.menu = OptionsMenu()
        screen = OptionsMenuScreen(self.menu)
        cmds = {commands.EXIT:self.stopRunning}
        PygameController.__init__(self, screen, commands=cmds)
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running