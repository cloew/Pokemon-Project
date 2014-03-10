
class EntryDelegate:
    """ Represents an action to perform when entering a Tile """
    
    def __init__(self):
        """ Initialize the Entry Delegate """
        self.callback = None
        
    def setCallback(self, callback):
        """ Set the Entry Delegate callback """
        self.callback = callback
        
    def onEnter(self):
        """ Perform on Enter event """
        self.callback(["Entered a tile"])