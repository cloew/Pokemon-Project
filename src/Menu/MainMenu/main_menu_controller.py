from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.GUI.screen import screen

from Menu.MainMenu.main_menu import MainMenu
from Screen.GUI.MainMenu.main_menu_view import MainMenuScreen


class MainMenuController:
    """ Controller for the main menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        self.menu = MainMenu()
        self.menuScreen = MainMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.EXIT:self.menu.quit,
                           commands.SELECT:self.menu.enter}
        
    def run(self):
        """ Runs the game loop """
        while self.menu.running:
            screen.setScreen(self.menuScreen)
            screen.update()
            inputProcessor.processInputs(self.cmds)
            screen.draw()