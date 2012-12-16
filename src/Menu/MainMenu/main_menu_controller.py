from Controller.controller import Controller
from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor

from Menu.MainMenu.main_menu import MainMenu
from Screen.Console.Menu.MainMenu.main_menu_screen import MainMenuScreen

class MainMenuController(Controller):
    """ Controller for the main menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        self.menu = MainMenu()
        self.screen = MainMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.EXIT:self.menu.quit,
                           commands.SELECT:self.menu.enter}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running