from Screen.Pygame.MessageBox.message_box import MessageBox
from Screen.Pygame.screen import Screen

class MessageBoxScreen(Screen):
    """ Represents a message box screen """
    
    def __init__(self, message):
        """ Initialize the Message Box Screen """
        self.messageBox = MessageBox(message)
        
    def draw(self, window):
        """ Draw the Screen """
        text = self.messageBox.draw()
        textpos = self.getCenteredRect(window, text, .5, .75)
        window.draw(text, textpos)
        
    def update(self):
        """ Update the Screen """
        self.messageBox.update()