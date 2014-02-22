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
    
    def __init__(self, trainer, zone, doneCallback=None):
        """ Initialize the Zone Controller """
        self.zone = zone
        self.doneCallback = doneCallback
        self.zone.setCallbacks(self.interactWithPerson)
        self.playerPerson = TrainerPerson(self.zone.tiles[1][1], "trainer", trainer)
        
        screen = ZoneScreen(self.playerPerson, self.zone)
        
        cmds = {commands.UP:self.playerPerson.up,
                (commands.UP, RELEASED):self.playerPerson.stopMovingUp,
                commands.DOWN:self.playerPerson.down,
                (commands.DOWN, RELEASED):self.playerPerson.stopMovingDown,
                commands.LEFT:self.playerPerson.left,
                (commands.LEFT, RELEASED):self.playerPerson.stopMovingLeft,
                commands.RIGHT:self.playerPerson.right,
                (commands.RIGHT, RELEASED):self.playerPerson.stopMovingRight,
                commands.SELECT:self.select,
                commands.EXIT:self.stopRunning}
        
        PygameController.__init__(self, screen, commands=cmds)
                     
    def select(self):
        """ Performs a Select """
        self.playerPerson.interactWithAdjacentTile()
        
    def interactWithPerson(self, otherPerson, message):
        """ Interact with the given person """
        self.runController(MessageBoxController(BattleMessage(message), self.screen))
        
        if otherPerson.isBattleable():
            self.runController(BattleController(self.playerPerson.trainer, otherPerson.trainer))
            if self.doneCallback is not None and self.doneCallback():
                self.stopRunning()
        
    def performGameCycle(self):
        """ Move the Trainer if needed in this tick """
        self.playerPerson.performGameTick()
        