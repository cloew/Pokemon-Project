from Controller.controller import Controller
from InputProcessor import commands

#from Screen.GUI.Battle.action_screen import ActionScreen

class ActionController(Controller):
    """ Controller for selection a Battle Action """
    
    def __init__(self, battle):
        """ Builds the Action Controller """
        self.battle = battle
        #self.actionScreen = ActionScreen(self.battle)
        self.action = None
        self.cmds = {commands.SELECT:self.battle.select}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.battleScreen
        
    def running(self):
        """ Return if the controller is still running """
        return self.action is None 