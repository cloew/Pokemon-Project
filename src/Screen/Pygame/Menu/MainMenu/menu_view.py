from Screen.Pygame.Menu.menu_widget import MenuWidget
from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image

class MenuView(MenuWidget):
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        surface = self.buildSurface()
        width = surface.get_width()
        height = surface.get_height()
        MenuWidget.__init__(self, menu, width, height)
        
    def buildSurface(self):
        """ Build the Men Surface """
        return self.getMenu()
        
    def getMenu(self):
        """ Build the Surface for the menu """
        return load_image(GetImagePath("menu.png"))