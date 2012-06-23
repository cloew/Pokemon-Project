from Controller.controller import Controller
from InputProcessor import commands

from Battle.battle import Battle
#from Screen.GUI.Battle.battle_screen import BattleScreen

class BattleController(Controller):
    """ Controller for a pokemon battle """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the Battle Controller """
        self.battle = Battle(playerTrainer, oppTrainer)
        #self.battleScreen = BattleScreen(self.battle)
        self.cmds = {}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        #return self.menuScreen
        
    def running(self):
        """ Return if the controller is still running """
        return not self.battle.over