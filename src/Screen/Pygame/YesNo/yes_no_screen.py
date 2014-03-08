from kao_gui.pygame.pygame_screen import PygameScreen

class YesNoScreen(PygameScreen):
    """ Represents the screen for Picking Yes/No """
    
    def __init__(self, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.lastScreen = lastScreen
        self.messageBox = None
        
    def drawSurface(self):
        """ Draws the screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        if self.messageBox is not None:
            messageBoxSurface = self.messageBox.draw()
            self.drawOnSurface(messageBoxSurface, left=.025, top=.7)