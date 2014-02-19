from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class TwoColumnMenuView(SizedWidget):
    """ Represents a Two Column Menu View """
    
    def __init__(self, menu, width, height):
        """ Initialize the Two Column Menu View """
        SizedWidget.__init__(self, width, height)
        self.menu = menu
        
        self.entries = []
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
        
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