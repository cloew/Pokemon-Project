from Battle.battle_message import BattleMessage
from InputProcessor import commands

from Screen.Pygame.Event.zone_event_handler import PerformEvents
from Screen.Pygame.Menu.ZoneMenu.zone_menu_controller import ZoneMenuController
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.Zone.zone_screen import ZoneScreen

from Zone.zone import Zone
from Zone.zone_factory import ZoneFactory
from Zone.Person.trainer_person import TrainerPerson

from collections import deque
from kao_gui.pygame.key_states import PRESSED, RELEASED
from kao_gui.pygame.pygame_controller import PygameController

class ZoneController(PygameController):
    """ Controller for a Zone """
    
    def __init__(self, trainer, zone, row, column, doneCallback=None):
        """ Initialize the Zone Controller """
        self.zone = zone
        self.doneCallback = doneCallback
        self.zone.setCallbacks(self.handleZoneEvents)
        self.playerPerson = TrainerPerson(self.zone.tiles[row][column], "trainer", trainer, causeEnterEvents=True)
        
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
                commands.EXIT:self.runZoneMenu}
        
        PygameController.__init__(self, screen, commands=cmds)
                     
    def select(self):
        """ Performs a Select """
        self.playerPerson.interactWithAdjacentTile()
        
    def runZoneMenu(self):
        """ Run the Zone Menu """
        self.runController(ZoneMenuController(self))
        
    def handleZoneEvents(self, events):
        """ Handle Zone Events """
        PerformEvents(deque(events), self)
        
        if self.doneCallback is not None and self.doneCallback():
            self.stopRunning()
        
    def performGameCycle(self):
        """ Move the Trainer if needed in this tick """
        self.playerPerson.performGameTick()
        
    def setupZone(self, zone, row, column):
        """ Setup the current zone """
        self.zone = zone
        self.zone.setCallbacks(self.handleZoneEvents)
        self.playerPerson.setTile(self.zone.tiles[row][column])
        
        self.screen.playerPerson = self.playerPerson
        self.screen.zone = self.zone
        
        self.commands[commands.UP] = self.playerPerson.up
        self.commands[(commands.UP, RELEASED)] = self.playerPerson.stopMovingUp
        self.commands[commands.DOWN] = self.playerPerson.down
        self.commands[(commands.DOWN, RELEASED)] = self.playerPerson.stopMovingDown
        self.commands[commands.LEFT] = self.playerPerson.left
        self.commands[(commands.LEFT, RELEASED)] = self.playerPerson.stopMovingLeft
        self.commands[commands.RIGHT] = self.playerPerson.right
        self.commands[(commands.RIGHT, RELEASED)] = self.playerPerson.stopMovingRight