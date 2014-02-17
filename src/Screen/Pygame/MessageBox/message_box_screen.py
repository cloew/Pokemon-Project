from Screen.Pygame.MessageBox.message_box import MessageBox

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.pygame_screen import PygameScreen

class MessageBoxScreen(PygameScreen):
    """ Represents a message box screen """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Message Box Screen """
        self.messageBox = MessageBox(message)
        self.lastScreen = lastScreen
        
    def drawSurface(self, surface):
        """ Draw the Screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        width = surface.get_width()*.9
        height = surface.get_height()*.3
        
        messageBoxWindowSurface = GetTransparentSurface(width, height)
        messageBoxSurface = self.messageBox.draw()
        
        messageBoxPosition = messageBoxSurface.get_rect(centerx=width*.5, centery=height*.5)
        messageBoxWindowSurface.blit(messageBoxSurface, messageBoxPosition)
        self.drawOnSurface(messageBoxWindowSurface, left=.05, top=.7)
        
    def update(self):
        """ Update the Screen """
        self.lastScreen.update()
        self.messageBox.update()