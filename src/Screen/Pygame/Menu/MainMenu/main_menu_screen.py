from scrolling_map import map
from logo import Logo
from menu_view import MenuView

from kao_gui.pygame.pygame_screen import PygameScreen

class MainMenuScreen(PygameScreen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def drawSurface(self, surface):
        """ Draws the screen to the provided window """
        self.drawMap(surface)
        self.drawLogo(surface)
        self.drawMenu(surface)
        
    def drawMap(self, surface):
        """ Draws the map to the window """
        mapSurface = map.draw()
        surface.blit(mapSurface, (0, 0))
        
    def drawLogo(self, surface):
        """ Draws the Logo to the window """
        logoSurface = self.logo.draw()
        logoPosition = self.getCenteredPostition(logoSurface, .5, .25) 
        surface.blit(logoSurface, logoPosition)
        
    def drawMenu(self, surface):
        """ Draws the Menu to the window """
        menuSurface = self.menuView.draw()
        menuPosition = self.getCenteredPostition(menuSurface, .5, 11.0/16)
        surface.blit(menuSurface, menuPosition)
        