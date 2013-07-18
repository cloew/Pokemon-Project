from Screen.Pygame.Controller.controller import Controller
from InputProcessor import commands

from Menu.TrainerMenu.trainer_menu import TrainerMenu
from Screen.Pygame.Battle.battle_controller import BattleController
from Screen.Pygame.Menu.TrainerMenu.trainer_menu_screen import TrainerMenuScreen

from Trainer.trainer_factory import TrainerFactory

class TrainerMenuController(Controller):
    """ Controller for the trainer select menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        Controller.__init__(self)
        self.menu = TrainerMenu(self.performBattle)
        self.screen = TrainerMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.EXIT:self.exit,
                     commands.SELECT:self.menu.enter}
                     
    def performBattle(self, entry):
        """ Perform a Battle """
        enemy = TrainerFactory.loadFromXML("Badass", "Eric", TrainerFactory.COMPUTER)
        battleController = BattleController(entry.trainer, enemy)
        battleController.run()
        
    def exit(self):
        """ Return if the controller is still running """
        return self.stopRunning()