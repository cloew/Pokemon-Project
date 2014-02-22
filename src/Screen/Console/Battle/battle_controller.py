from Battle.battle import Battle

from Screen.Console.Battle.battle_message_controller import BattleMessageController
from Screen.Console.Battle.battle_round_controller import BattleRoundController
from Screen.Console.Battle.battle_message_screen import BattleMessageScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class BattleController(ConsoleController):
    """ Controller for a pokemon battle """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the Battle Controller """
        self.battle = Battle(playerTrainer, oppTrainer)
        screen = BattleMessageScreen(self.battle)
        
        ConsoleController.__init__(self, screen)
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        self.runController(BattleMessageController(self.battle, self.screen))
        self.runController(BattleRoundController(self.battle, self.screen))
        self.runController(BattleMessageController(self.battle, self.screen))
        
        self.stopRunning()