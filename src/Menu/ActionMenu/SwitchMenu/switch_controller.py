from Controller.controller import Controller
from InputProcessor import commands

from switch_menu import SwitchMenu
from Screen.Console.Menu.ActionMenu.action_menu_screen import ActionMenuScreen # Need differnet screen

class SwitchController(Controller):
    """ Controller for selecting a Battle Switch Action """
    
    def __init__(self, user, targets):
        """ Builds the Action Controller """
        self.goBack = False
        self.menu = SwitchMenu(user, targets)
        self.screen = ActionMenuScreen(self.menu) # Need different screen
        self.cmds = {commands.SELECT:self.menu.enter,
                     commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.RIGHT:self.menu.right,
                     commands.LEFT:self.menu.left,
                     commands.EXIT:self.back}
        
    def running(self):
        """ Return whether the controller is still running """
        return (self.menu.action is None) and (not self.goBack)

    def back(self):
        """ Return to the Action Menu """
        self.goBack = True