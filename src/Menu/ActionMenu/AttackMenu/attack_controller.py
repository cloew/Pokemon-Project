from Controller.controller import Controller
from InputProcessor import commands

from attack_menu import AttackMenu
from Screen.Console.Menu.ActionMenu.action_menu_screen import ActionMenuScreen

class AttackController(Controller):
    """ Controller for selecting a Battle Attack Action """
    
    def __init__(self, user, targets):
        """ Builds the Attack Controller """
        self.goBack = False
        self.menu = AttackMenu(user, targets)
        self.screen = ActionMenuScreen(self.menu)
        self.cmds = {commands.SELECT:self.menu.enter,
                     commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.RIGHT:self.menu.right,
                     commands.LEFT:self.menu.left,
                     commands.EXIT:self.back}
        
    def running(self):
        """ Return if the controller is still running """
        return (self.menu.action is None) and (not self.goBack)

    def back(self):
        """ Return to the Action Menu """
        self.goBack = True