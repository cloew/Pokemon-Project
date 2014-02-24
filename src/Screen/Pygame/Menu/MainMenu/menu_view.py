from menu_entry_view import MenuEntryView
from resources.resource_manager import GetImagePath

from Screen.Pygame.Menu.menu_widget import MenuWidget

from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_widget import PygameWidget

class MenuView(MenuWidget):
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        # self.entries = []
        surface = self.buildSurface()
        width = surface.get_width()
        height = surface.get_height()
        MenuWidget.__init__(self, menu, width, height)
        
        # numberOfEntries = len(menu.entries)
        # for entry in menu.entries:
            # entryView = MenuEntryView(entry, width=width, height=height/numberOfEntries)
            # self.entries.append(entryView)
        
    def buildSurface(self):
        """ Build the Men Surface """
        return self.getMenu()
        
    # def drawSurface(self): 
        # """ Draw the menu """
        # self.drawEntries()
        
    # def drawEntries(self):
        # """ Draws the menu entries on the Menu Surface """
        # for entry in self.entries:
            # entrySurface = entry.draw()
            # yRatio = (self.entries.index(entry) + 1)/4.0
            # self.drawOnSurface(entrySurface, centerx=.5, top=self.entries.index(entry)/3.0)
        
    def getMenu(self):
        """ Build the Surface for the menu """
        return load_image(GetImagePath("menu.png"))