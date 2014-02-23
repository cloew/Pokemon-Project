from kao_gui.pygame.widgets.label import Label
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class AttackMenuEntryWidget(MenuEntryView):
    """ Represents the widget for an Attack Menu Entry """
    
    def __init__(self, entry, width=0, height=0):
        """ Initialize the widget """
        MenuEntryView.__init__(self, entry, fontSize=28, width=width, height=height)
        self.entry = entry
        
        self.typeLabel = Label(entry.attack.type, size=18)
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.mainLabel.draw(), centerx=.5, centery=.3)
        self.drawOnSurface(self.typeLabel.draw(), centerx=.3, centery=.65)