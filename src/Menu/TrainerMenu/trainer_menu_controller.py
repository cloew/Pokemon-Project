from Controller.controller import Controller
from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.GUI.screen import screen

from Menu.TrainerMenu.trainer_menu import TrainerMenu
from Screen.GUI.TrainerMenu.trainer_menu_view import TrainerMenuScreen

class TrainerMenuController(Controller):
    """ Controller for the trainer select menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        self.menu = TrainerMenu()
        self.menuScreen = TrainerMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.EXIT:self.menu.quit,
                           commands.SELECT:self.menu.enter}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.menuScreen