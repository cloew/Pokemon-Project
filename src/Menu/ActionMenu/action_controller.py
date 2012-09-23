from Controller.controller import Controller
from InputProcessor import commands

from action_menu import ActionMenu
#from Screen.GUI.Battle.action_screen import ActionScreen

class ActionController(Controller):
    """ Controller for selection a Battle Action """
    
    def __init__(self, battle):
        """ Builds the Action Controller """
        self.battle = battle
        #self.actionScreen = ActionScreen(self.battle)
        self.menu = ActionMenu()
        self.cmds = {commands.SELECT:self.actionMenu.enter,
                           commands.UP:self.actionMenu.up,
                           commands.DOWN:self.actionMenu.down,
                           commands.RIGHT:self.actionMenu.right,
                           commands.LEFT:self.actionMenu.left}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        #return self.actionScreen
        return None
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.action is None 