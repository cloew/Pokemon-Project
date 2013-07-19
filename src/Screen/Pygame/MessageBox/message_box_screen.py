from Screen.Pygame.MessageBox.message_box import MessageBox
from Screen.Pygame.screen import Screen

class MessageBoxScreen(Screen):
    """ Represents a message box screen """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Message Box Screen """
        self.messageBox = MessageBox(message)
        self.lastScreen = lastScreen
        
    def draw(self, window):
        """ Draw the Screen """
        self.lastScreen.draw(window)
        
        text = self.messageBox.draw()
        textpos = self.getCenteredRect(window, text, .5, .75)
        window.draw(text, textpos)
        
    def update(self):
        """ Update the Screen """
        self.lastScreen.update()
        self.messageBox.update()