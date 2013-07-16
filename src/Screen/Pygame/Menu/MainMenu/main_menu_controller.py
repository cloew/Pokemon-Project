from InputProcessor import commands
from Menu.MainMenu.main_menu import MainMenu
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.MainMenu.main_menu_screen import MainMenuScreen

class MainMenuController(Controller):
    """ Controller for the Pygame Main Menu """
    
    def __init__(self):
        """ Initialize the Main Menu Controller """
        self.menu = MainMenu()
        self.screen = MainMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.EXIT:self.menu.quit,
                     commands.SELECT:self.menu.enter}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running