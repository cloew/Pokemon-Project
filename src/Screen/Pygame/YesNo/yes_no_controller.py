from InputProcessor import commands
from Screen.Pygame.YesNo.yes_no_screen import YesNoScreen

from kao_gui.pygame.pygame_controller import PygameController

class YesNoController(PygameController):
    """ Controller for picking Yes or No """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Yes/No Controller """
        screen = YesNoScreen(message, lastScreen)
        cmds = {commands.SELECT:self.select,
                commands.EXIT:self.back}
        PygameController.__init__(self, screen, commands=cmds)
        self.answer = False
        
    def select(self):
        """ Select the current entry """
        
    def back(self):
        """ Return to the previous """
        self.answer = False
        self.stopRunning()