from Menu.TrainerMenu.trainer_menu import TrainerMenu
from Trainer.trainer_factory import TrainerFactory

from Screen.Console.Battle.battle_controller import BattleController
from Screen.Console.Menu.TrainerMenu.trainer_menu_screen import TrainerMenuScreen

from kao_console.ascii import KAO_UP, KAO_DOWN, ENDL
from kao_gui.console.console_controller import ConsoleController

class TrainerMenuController(ConsoleController):
    """ Controller for the trainer select menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        self.menu = TrainerMenu(self.play)
        screen = TrainerMenuScreen(self.menu)
        cmds = {KAO_UP:self.menu.up,
                KAO_DOWN:self.menu.down,
                ENDL:self.menu.enter}
        ConsoleController.__init__(self, screen, commands=cmds, cancellable=True)
        
    def play(self, entry=None):
        """ Play a Battle with the Trainer from the entry """
        enemy = TrainerFactory.loadFromXML("Badass", "Eric", TrainerFactory.COMPUTER)
        self.runController(BattleController(entry.trainer, enemy))