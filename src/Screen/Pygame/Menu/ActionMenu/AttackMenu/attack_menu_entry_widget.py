from kao_gui.pygame.widgets.label import Label
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class AttackMenuEntryWidget(SizedWidget):
    """ Represents the widget for an Attack Menu Entry """
    
    def __init__(self, entry, width=0, height=0):
        """ Initialize the widget """
        SizedWidget.__init__(self, width, height)
        self.entry = entry
        
        self.attackLabel = Label(entry.getText(), size=28)
        
    def update(self):
        """ Update the Entry Widget """
        self.attackLabel.setBold(self.entry.selected)
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.attackLabel.draw(), centerx=.5, centery=.5)