from InputProcessor import commands
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.MessageBox.message_box_screen import MessageBoxScreen

class MessageBoxController(Controller):
    """ Controller for a Message Box """
    
    def __init__(self, message):
        """ Initialize the Message Box Controller """
        Controller.__init__(self)
        self.message = message
        self.screen = MessageBoxScreen(message)
        self.cmds = {commands.SELECT:self.closeMessageBox}
        
    def closeMessageBox(self):
        """ Close the message box if it has finished showing """
        if self.message.fullyDisplayed:
            self.stopRunning()
        
    def update(self):
        """ Do Nothing """