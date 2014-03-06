from Screen.Pygame.MessageBox.message_box import MessageBox

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.pygame_screen import PygameScreen

class YesNoScreen(PygameScreen):
    """ Represents the screen for Picking Yes/No """
    
    def __init__(self, message, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.lastScreen = lastScreen
        self.messageBox = MessageBox(message, fullyDisplay=True)
        
    def drawSurface(self):
        """ Draws the screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        width = self.width*.9
        height = self.height*.3
        
        messageBoxWindowSurface = GetTransparentSurface(width, height)
        messageBoxSurface = self.messageBox.draw()
        
        messageBoxPosition = messageBoxSurface.get_rect(centerx=width*.5, centery=height*.5)
        messageBoxWindowSurface.blit(messageBoxSurface, messageBoxPosition)
        self.drawOnSurface(messageBoxWindowSurface, left=.05, top=.7)