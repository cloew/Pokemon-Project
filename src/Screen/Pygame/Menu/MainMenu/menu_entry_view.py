from kao_gui.pygame.widgets.label import Label

class MenuEntryView(Label):
    """ Represents an entry in the menu """
    
    def __init__(self, entry, fontSize=36):
        """ Sets the entry's text """
        Label.__init__(self, entry.getText(), size=fontSize)
        self.entry = entry
        
    def update(self):
        """ Update the Entry Widget """
        self.setBold(self.entry.selected)