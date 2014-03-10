
class EntryDelegate:
    """ Represents an action to perform when entering a Tile """
    
    def __init__(self):
        """ Initialize the Entry Delegate """
        self.callback = None
        
    def setCallback(self, callback):
        """ Set the Entry Delegate callback """
        self.callback = callback
        
    def onEnter(self, player):
        """ Perform on Enter event """
        player.stopMovingUp()
        player.stopMovingDown()
        player.stopMovingLeft()
        player.stopMovingRight()
        self.callback(["Entered a tile"])