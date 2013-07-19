from InputProcessor import commands
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
        self.trainer = TrainerPositionWrapper(trainer, self.zone.tiles[0][0])
        self.screen = ZoneScreen(self.zone, self.trainer)
        
        self.cmds = {commands.EXIT:self.stopRunning}