from scrolling_map import map
from logo import Logo
from main_menu_widget import MainMenuWidget

from kao_gui.pygame.pygame_screen import PygameScreen
from kao_gui.pygame.widgets.label import Label

class MainMenuScreen(PygameScreen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu, currentPlayer):
        """  """
        PygameScreen.__init__(self)
        self.currentPlayer = currentPlayer
        self.menu = menu
        self.logo = Logo()
        
        name = "None"
        if currentPlayer is not None:
            name = currentPlayer.fullname
        self.playerLabel = Label("{0}: {1}".format("Player", name), size=24, color=(0, 0, 0))
        
        self.menuView = MainMenuWidget(menu)
        
    def drawSurface(self):
        """ Draws the screen to the provided window """
        self.drawMap()
        self.drawOnSurface(self.playerLabel.draw(), right=1, top=0)
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
        