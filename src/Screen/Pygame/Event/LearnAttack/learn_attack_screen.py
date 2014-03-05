from kao_gui.pygame.pygame_screen import PygameScreen

class LearnAttackScreen(PygameScreen):
    """ Represents the screen for Learning an Attack """
    
    def __init__(self, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.lastScreen = lastScreen
        
    def drawSurface(self):
        """ Draws the screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)