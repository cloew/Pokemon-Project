from Battle.battle_message import BattleMessage
from InputProcessor import commands
from InputProcessor.key_states import PRESSED, RELEASED

from Screen.Pygame.Battle.battle_controller import BattleController
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.Zone.zone_screen import ZoneScreen

from Zone.zone import Zone
from Zone.Person.trainer_person import TrainerPerson
from Zone.Person.Interaction.interaction_delegate import InteractionDelegate

class ZoneController(Controller):
    """ Controller for a Zone """
    
    def __init__(self, trainer):
        """ Initialize the Zone Controller """
        Controller.__init__(self)
        self.zone = Zone(self.interactWithTrainer)
        self.trainer = TrainerPerson(self.zone.tiles[1][1], "trainer", trainer, InteractionDelegate("", self.interactWithTrainer))
        
        self.screen = ZoneScreen(self.zone)
        
        self.trainerToBattle = None
        
        self.cmds = {commands.UP:self.trainer.up,
                     (commands.UP, RELEASED):self.trainer.stopMovingUp,
                     commands.DOWN:self.trainer.down,
                     (commands.DOWN, RELEASED):self.trainer.stopMovingDown,
                     commands.LEFT:self.trainer.left,
                     (commands.LEFT, RELEASED):self.trainer.stopMovingLeft,
                     commands.RIGHT:self.trainer.right,
                     (commands.RIGHT, RELEASED):self.trainer.stopMovingRight,
                     commands.SELECT:self.select,
                     commands.EXIT:self.stopRunning}
                     
    def select(self):
        """ Performs a Select """
        self.trainer.interactWithAdjacentTile()
        
    def interactWithTrainer(self, trainer, message):
        """ Interact with the given trainer """
        messageBoxController = MessageBoxController(BattleMessage(message), self.screen)
        messageBoxController.run()
        
        if trainer.isBattleable():
            battleController = BattleController(self.trainer.trainer, trainer.trainer)
            battleController.run()
        
    def update(self):
        """ Try to battle if necessary """
        self.trainer.performGameTick()
        