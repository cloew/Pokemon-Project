from Controller.controller import Controller
from InputProcessor import commands

from Battle.battle import Battle
from Screen.Console.Battle.battle_screen import BattleScreen

class BattleController(Controller):
    """ Controller for a pokemon battle """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the Battle Controller """
        self.battle = Battle(playerTrainer, oppTrainer)
        self.screen = BattleScreen(self.battle)
        self.cmds = {commands.SELECT:self.battle.select}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.battleScreen
        
    def running(self):
        """ Return if the controller is still running """
        return not self.battle.over # not quite since I need to show the aftermath of the battle, whiting out, or rewards
        
    def update(self):
        """ Tells the battle object what to perform """
        self.battle.update()