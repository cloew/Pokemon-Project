from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class TwoColumnMenuView(SizedWidget):
    """ Represents a Two Column Menu View """
    
    def __init__(self, menu, width, height, MenuEntryView=MenuEntryView):
        """ Initialize the Two Column Menu View """
        SizedWidget.__init__(self, width, height)
        self.menu = menu
        
        self.entries = []
        widthPerEntry = width/2.0
        heightPerEntry = height/2.0
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry, width=widthPerEntry, height=heightPerEntry))
        
    def drawSurface(self):
        """ Draw the Battle Menu View """
        for entry in self.entries:
            entrySurface = entry.draw()
            row, column = self.menu.getPosition(entry.entry)
            print entry.entry.getText(), row, column
            self.drawOnSurface(entrySurface, left=column/2.0, top=row/2.0)
            
    def getXRatio(self, i):
        """ Returns the xRatio of the entry at i """
        return ((i%2)*2+ 1)/4.0
        
    def getYRatio(self, i):
        """ Returns the yRatio of the entry at i """
        return ((i/2)+ 1)/3.0