from Controller.controller import Controller
from InputProcessor import commands

from action_menu import ActionMenu
from Screen.GUI.ActionMenu.action_menu_screen import ActionMenuScreen

class ActionController(Controller):
    """ Controller for selection a Battle Action """
    
    def __init__(self, battle):
        """ Builds the Action Controller """
        self.battle = battle
        self.menu = ActionMenu()
        self.actionScreen = ActionMenuScreen(self.menu)
        self.cmds = {commands.SELECT:self.menu.enter,
                           commands.UP:self.menu.up,
                           commands.DOWN:self.menu.down,
                           commands.RIGHT:self.menu.right,
                           commands.LEFT:self.menu.left}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.actionScreen
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.action is None 