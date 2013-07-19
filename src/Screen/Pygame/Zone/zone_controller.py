from Battle.battle_message import BattleMessage
from InputProcessor import commands
from InputProcessor.key_states import PRESSED, RELEASED

from Screen.Pygame.Battle.battle_controller import BattleController
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Zone.zone_screen import ZoneScreen

from Zone.trainer_position_wrapper import TrainerPositionWrapper
from Zone.zone import Zone

class ZoneController(Controller):
    """ Controller for a Zone """
    
    def __init__(self, trainer):
        """ Initialize the Zone Controller """
        Controller.__init__(self)
        self.zone = Zone()
        self.trainer = TrainerPositionWrapper(trainer, self.zone.tiles[1][1])
        self.zone.enemyTrainer.message = "Hi! I'm Eric!"
        self.zone.enemyTrainer.interactionCallback = self.interactWithTrainer
        self.screen = ZoneScreen(self.zone)
        
        self.trainerToBattle = None
        
        self.cmds = {commands.UP:self.trainer.up,
                     (commands.UP, RELEASED):self.trainer.stopMoving,
                     commands.DOWN:self.trainer.down,
                     (commands.DOWN, RELEASED):self.trainer.stopMoving,
                     commands.LEFT:self.trainer.left,
                     (commands.LEFT, RELEASED):self.trainer.stopMoving,
                     commands.RIGHT:self.trainer.right,
                     (commands.RIGHT, RELEASED):self.trainer.stopMoving,
                     commands.SELECT:self.select,
                     commands.EXIT:self.stopRunning}
                     
    def select(self):
        """ Performs a Select """
        if self.screen.isShowingMessage() and self.screen.messageBox.isFullyShown():
            self.screen.stopShowingMessage()
        else:
            self.trainer.interactWithAdjacentTile()
        
    def interactWithTrainer(self, trainer, message):
        """ Interact with the given trainer """
        self.screen.showMessage(BattleMessage(message))
        if trainer.isBattleable():
            self.trainerToBattle = trainer.trainer
        
    def update(self):
        """ Try to battle if necessary """
        self.trainer.performGameTick()
        
        if not self.screen.isShowingMessage() and self.trainerToBattle is not None:
            battleController = BattleController(self.trainer.trainer, self.trainerToBattle)
            battleController.run()
            self.trainerToBattle = None
        