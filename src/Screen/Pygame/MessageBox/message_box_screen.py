from Screen.Pygame.Menu.menu_background_widget import MenuBackgroundWidget
from Screen.Pygame.MessageBox.message_box import MessageBox

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.pygame_screen import PygameScreen

class MessageBoxScreen(PygameScreen):
    """ Represents a message box screen """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Message Box Screen """
        PygameScreen.__init__(self)
        self.messageBox = MessageBox(self.width*.95, self.height*.3, message)
        self.lastScreen = lastScreen
        
    def drawSurface(self):
        """ Draw the Screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        messageBoxSurface = self.messageBox.draw()
        self.drawOnSurface(messageBoxSurface, left=.025, top=.7)
        
    def update(self):
        """ Update the Screen """
        self.lastScreen.update()
        self.messageBox.update()