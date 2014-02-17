from InputProcessor import commands
from Marathon.marathon import Marathon

from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Marathon.marathon_screen import MarathonScreen
from Screen.Pygame.Zone.zone_controller import ZoneController

from kao_gui.pygame.pygame_controller import PygameController

class MarathonController(PygameController):
    """ Controller for a Marathon """
    
    def __init__(self, trainer):
        """ Initialize the Marathon Controller """
        self.marathon = Marathon()
        self.trainer = trainer
        screen = MarathonScreen(self.marathon)
        
        cmds = {commands.SELECT:self.select,
                commands.EXIT:self.stopRunning}
        PygameController.__init__(self, screen, commands=cmds)
                     
    def select(self):
        """ Performs a Select """
        self.runController(ZoneController(self.trainer, zone=self.marathon.zone))
        