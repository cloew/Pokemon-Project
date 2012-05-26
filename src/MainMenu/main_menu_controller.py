import sys
sys.path.append("C:\\cygwin\\home\\Programming\\Pokemon-Python\\src")

from MainMenu.main_menu import MainMenu
from Screen.GUI.screen import Screen
from Screen.GUI.MainMenu.main_menu_view import MainMenuScreen


class MainMenuController:
    """ Controller for the main menu """
    
    def __init__(self, screen):
        """ Builds the Main Menu Controller """
        self.menu = MainMenu()
        self.screen = screen
        self.menuScreen = MainMenuScreen(self.menu)
        self.screen.setScreen(self.menuScreen)
        self.cmds = {}
        
    def run(self):
        """ Runs the game loop """
        while self.menu.running:
            self.screen.update()
            self.screen.processEvents()
            self.screen.draw()
                
if __name__ == "__main__":
    screen = Screen()
    main_controller = MainMenuController(screen)
    main_controller.run()