from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.pygame_widget import PygameWidget

class TwoColumnMenuView(PygameWidget):
    """ Represents a Two Column Menu View """
    
    def __init__(self, menu):
        """ Initialize the Two Column Menu View """
        self.menu = menu
        
        self.entries = []
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
            
    def setSize(self, width, height):
        """ Set the surface size """
        self.__width = width
        self.__height = height
        
        for entry in self.entries:
            entry.setSize((width*.9)/self.menu.columns, (height*.9)/self.menu.columns)
            
    def buildSurface(self):
        """ Return the surface for the widget """
        return GetTransparentSurface(self.__width, self.__height)
        
    def drawSurface(self):
        """ Draw the Battle Menu View """
        for entry in self.entries:
            entrySurface = entry.draw()
            index = self.entries.index(entry)
            xRatio  = self.getXRatio(index)
            yRatio = self.getYRatio(index)
            self.drawOnSurface(entrySurface, centerx=xRatio, centery=yRatio)
            
    def getXRatio(self, i):
        """ Returns the xRatio of the entry at i """
        return ((i%2)*2+ 1)/4.0
        
    def getYRatio(self, i):
        """ Returns the yRatio of the entry at i """
        return ((i/2)+ 1)/3.0