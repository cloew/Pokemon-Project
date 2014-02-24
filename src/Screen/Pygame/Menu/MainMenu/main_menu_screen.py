from scrolling_map import map
from logo import Logo
from main_menu_widget import MainMenuWidget

from kao_gui.pygame.pygame_screen import PygameScreen

class MainMenuScreen(PygameScreen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        PygameScreen.__init__(self)
        self.menu = menu
        self.logo = Logo()
        self.menuView = MainMenuWidget(menu)
        
    def drawSurface(self):
        """ Draws the screen to the provided window """
        self.drawMap()
        self.drawLogo()
        self.drawMenu()
        
    def drawMap(self):
        """ Draws the map to the window """
        mapSurface = map.draw()
        self.drawOnSurface(mapSurface, left=0, top=0)
        
    def drawLogo(self):
        """ Draws the Logo to the window """
        logoSurface = self.logo.draw()
        self.drawOnSurface(logoSurface, centerx=.5, centery=.25)
        
    def drawMenu(self):
        """ Draws the Menu to the window """
        menuSurface = self.menuView.draw()
        self.drawOnSurface(menuSurface, centerx=.5, centery=11.0/16)
        