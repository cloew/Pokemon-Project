from InputProcessor import commands
from Marathon.marathon import Marathon

from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Marathon.marathon_screen import MarathonScreen
from Screen.Pygame.Zone.zone_controller import ZoneController

class MarathonController(Controller):
    """ Controller for a Marathon """
    
    def __init__(self, trainer):
        """ Initialize the Marathon Controller """
        Controller.__init__(self)
        
        self.marathon = Marathon()
        self.trainer = trainer
        self.screen = MarathonScreen(self.marathon)
        
        self.cmds = {commands.SELECT:self.select,
                     commands.EXIT:self.stopRunning}
                     
    def select(self):
        """ Performs a Select """
        zoneController = ZoneController(self.trainer, zone=self.marathon.zone)
        zoneController.run()
        