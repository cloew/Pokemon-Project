from Screen.Pygame.Menu.menu_with_background_widget import MenuWithBackgroundWidget

from kao_gui.pygame.pygame_screen import PygameScreen

class YesNoScreen(PygameScreen):
    """ Represents the screen for Picking Yes/No """
    
    def __init__(self, menu, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.lastScreen = lastScreen
        self.messageBox = None
        self.menuView = MenuWithBackgroundWidget(menu, .15*self.width, .2*self.height)
        
    def drawSurface(self):
        """ Draws the screen """
        previousScreenSurface = self.lastScreen.draw()
        self.drawOnSurface(previousScreenSurface, left=0, top=0)
        
        if self.messageBox is not None:
            messageBoxSurface = self.messageBox.draw()
            self.drawOnSurface(messageBoxSurface, left=.05, top=.7)
            
            menuSurface = self.menuView.draw()
            self.drawOnSurface(menuSurface, right=.95, centery=.6)