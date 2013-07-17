from Battle.battle import Battle
from InputProcessor import commands

from Screen.Pygame.Battle.battle_screen import BattleScreen
from Screen.Pygame.Battle.battle_introduction_controller import BattleIntroductionController
from Screen.Pygame.Controller.controller import Controller

class BattleController(Controller):
    """ Controller for a pokemon battle """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the Battle Controller """
        Controller.__init__(self)
        self.battle = Battle(playerTrainer, oppTrainer)
        self.screen = BattleScreen(self.battle)
        self.cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        
    def update(self):
        """ Tells the battle object what to perform """
        introductionController = BattleIntroductionController(self.battle, self.screen)
        introductionController.run()
        
        #if self.battle.over:
        self.stopRunning()