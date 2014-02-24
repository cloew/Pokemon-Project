from Screen.Pygame.Menu.menu_entry_widget import MenuEntryWidget

from kao_gui.pygame.widgets.label import Label

class AttackMenuEntryWidget(MenuEntryWidget):
    """ Represents the widget for an Attack Menu Entry """
    
    def __init__(self, entry, width, height):
        """ Initialize the widget """
        MenuEntryWidget.__init__(self, entry, fontSize=28, width=width, height=height)
        self.entry = entry
        
        self.typeLabel = Label(entry.attack.type, size=18)
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.mainLabel.draw(), centerx=.5, centery=.3)
        self.drawOnSurface(self.typeLabel.draw(), centerx=.3, centery=.65)