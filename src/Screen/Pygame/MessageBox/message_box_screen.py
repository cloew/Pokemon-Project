from Screen.Pygame.pygame_helper import GetTransparentSurface
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
        
        width = window.width*.9
        height = window.height*.3
        
        surface = GetTransparentSurface(width, height)
        messageBoxSurface = self.messageBox.draw()
        messageBoxPosition = messageBoxSurface.get_rect(centerx=width*.5, centery=height*.5)
        surface.blit(messageBoxSurface, messageBoxPosition)
        
        surfacePosition = surface.get_rect(left=window.width/20, top=window.height*.7)
        window.draw(surface, surfacePosition)
        
        
    def update(self):
        """ Update the Screen """
        self.lastScreen.update()
        self.messageBox.update()