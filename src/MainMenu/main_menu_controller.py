from InputProcessor import commands

from MainMenu.main_menu import MainMenu
from Screen.GUI.MainMenu.main_menu_view import MainMenuScreen


class MainMenuController:
    """ Controller for the main menu """
    
    def __init__(self, screen, inputProcessor):
        """ Builds the Main Menu Controller """
        self.menu = MainMenu()
        self.screen = screen
        self.menuScreen = MainMenuScreen(self.menu)
        self.screen.setScreen(self.menuScreen)
        self.cmds = {commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.EXIT:self.menu.quit,
                           commands.SELECT:self.menu.enter}
        self.inputProcessor = inputProcessor
        
    def run(self):
        """ Runs the game loop """
        while self.menu.running:
            self.screen.update()
            self.inputProcessor.processInputs(self.cmds)
            self.screen.draw()