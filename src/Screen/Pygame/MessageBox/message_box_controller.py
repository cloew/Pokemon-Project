from InputProcessor import commands
from Screen.Pygame.MessageBox.message_box_screen import MessageBoxScreen

from kao_gui.pygame.pygame_controller import PygameController

class MessageBoxController(PygameController):
    """ Controller for a Message Box """
    
    def __init__(self, message, lastScreen, autoClose=False):
        """ Initialize the Message Box Controller """
        self.message = message
        self.autoClose = autoClose
        
        screen = MessageBoxScreen(message, lastScreen)
        cmds = {commands.SELECT:self.closeMessageBox}
        
        PygameController.__init__(self, screen, commands=cmds)
        
    def performGameCycle(self):
        """ Perform the learn attack loop """
        if self.autoClose:
            self.closeMessageBox()
        
    def closeMessageBox(self):
        """ Close the message box if it has finished showing """
        if self.message.fullyDisplayed:
            self.stopRunning()