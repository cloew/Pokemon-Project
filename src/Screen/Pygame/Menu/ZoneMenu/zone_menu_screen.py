from Screen.Pygame.Menu.menu_with_background_widget import MenuWithBackgroundWidget

from kao_gui.pygame.pygame_screen import PygameScreen

class ZoneMenuScreen(PygameScreen):
    """ Represents the screen for the Zone Menu """
    
    def __init__(self, menu, lastScreen):
        """ Initialize the screen """
        PygameScreen.__init__(self)
        self.menuView = MenuWithBackgroundWidget(menu, self.width*.4, self.height)
        self.lastScreen = lastScreen
        
    def drawSurface(self):
        """ Draws the screen """
        screenSurface = self.lastScreen.draw()
        self.drawOnSurface(screenSurface, left=0, top=0)
        
        menuSurface = self.menuView.draw()
        self.drawOnSurface(menuSurface, right=1, top=0)