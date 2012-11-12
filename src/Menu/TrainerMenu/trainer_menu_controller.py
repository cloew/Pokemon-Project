from Controller.controller import Controller
from InputProcessor import commands

from Menu.TrainerMenu.trainer_menu import TrainerMenu
from Screen.Console.TrainerMenu.trainer_menu_screen import TrainerMenuScreen

class TrainerMenuController(Controller):
    """ Controller for the trainer select menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        self.menu = TrainerMenu()
        self.screen = TrainerMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.EXIT:self.menu.quit,
                           commands.SELECT:self.menu.enter}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running