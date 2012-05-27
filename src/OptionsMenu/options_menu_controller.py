from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.GUI.screen import screen

from OptionsMenu.options_menu import OptionsMenu
from Screen.GUI.OptionsMenu.options_menu_view import OptionsMenuScreen


class OptionsMenuController:
    """ Controller for the options menu """
    
    def __init__(self):
        """ Builds the Options Menu Controller """
        self.menu = OptionsMenu()
        self.optionsScreen = OptionsMenuScreen(self.menu)
        self.cmds = {commands.EXIT:self.menu.quit}
        
    def run(self):
        """ Runs the game loop """
        while self.menu.running:
            screen.setScreen(self.optionsScreen)
            screen.update()
            inputProcessor.processInputs(self.cmds)
            screen.draw()