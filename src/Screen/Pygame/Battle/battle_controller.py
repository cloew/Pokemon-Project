from Battle.battle import Battle
from InputProcessor import commands

from Screen.Pygame.Battle.battle_screen import BattleScreen
from Screen.Pygame.Battle.battle_aftermath_controller import BattleAftermathController
from Screen.Pygame.Battle.battle_introduction_controller import BattleIntroductionController
from Screen.Pygame.Battle.battle_round_controller import BattleRoundController

from kao_gui.pygame.pygame_controller import PygameController

class BattleController(PygameController):
    """ Controller for a pokemon battle """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the Battle Controller """
        self.battle = Battle(playerTrainer, oppTrainer)
        screen = BattleScreen(self.battle)
        PygameController.__init__(self, screen)
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        self.runController(BattleIntroductionController(self.battle, self.screen))
        self.runController(BattleRoundController(self.battle, self.screen))
        self.runController(BattleAftermathController(self.battle, self.screen))
        
        self.stopRunning()