from kao_gui.pygame.widgets.label import Label
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class MenuEntryWidget(SizedWidget):
    """ Represents an entry in the menu """
    
    def __init__(self, entry, width, height, fontSize=36):
        """ Sets the entry's text """
        SizedWidget.__init__(self, width, height)
        self.mainLabel = Label(entry.getText(), size=fontSize)
        self.entry = entry
        
    def update(self):
        """ Update the Entry Widget """
        self.mainLabel.setBold(self.entry.selected)
        self.mainLabel.setText(self.entry.getText())
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.mainLabel.draw(), centerx=.5, centery=.5)