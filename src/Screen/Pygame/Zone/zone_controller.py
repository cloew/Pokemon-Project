from Battle.battle_message import BattleMessage
from InputProcessor import commands

from Screen.Pygame.Battle.battle_controller import BattleController
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.Zone.zone_screen import ZoneScreen

from Zone.zone import Zone
from Zone.zone_factory import ZoneFactory
from Zone.Person.trainer_person import TrainerPerson
from Zone.Person.Interaction.interaction_delegate import InteractionDelegate

from kao_gui.pygame.key_states import PRESSED, RELEASED
from kao_gui.pygame.pygame_controller import PygameController

class ZoneController(PygameController):
    """ Controller for a Zone """
    
    def __init__(self, trainer, zone):
        """ Initialize the Zone Controller """
        self.zone = zone
        self.zone.setCallbacks(self.interactWithTrainer)
        self.trainer = TrainerPerson(self.zone.tiles[1][1], "trainer", trainer, 
                                     InteractionDelegate("", self.interactWithTrainer))
        
        screen = ZoneScreen(self.zone)
        
        cmds = {commands.UP:self.trainer.up,
                (commands.UP, RELEASED):self.trainer.stopMovingUp,
                commands.DOWN:self.trainer.down,
                (commands.DOWN, RELEASED):self.trainer.stopMovingDown,
                commands.LEFT:self.trainer.left,
                (commands.LEFT, RELEASED):self.trainer.stopMovingLeft,
                commands.RIGHT:self.trainer.right,
                (commands.RIGHT, RELEASED):self.trainer.stopMovingRight,
                commands.SELECT:self.select,
                commands.EXIT:self.stopRunning}
        
        PygameController.__init__(self, screen, commands=cmds)
                     
    def select(self):
        """ Performs a Select """
        self.trainer.interactWithAdjacentTile()
        
    def interactWithTrainer(self, trainer, message):
        """ Interact with the given trainer """
        self.runController(MessageBoxController(BattleMessage(message), self.screen))
        
        if trainer.isBattleable():
            self.runController(BattleController(self.trainer.trainer, trainer.trainer))
        
    def performGameCycle(self):
        """ Move the Trainer if needed in this tick """
        self.trainer.performGameTick()
        