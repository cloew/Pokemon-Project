
class TileContent:
    """ Represents content in a tile """
    
    def __init__(self, imageBaseName, interactionDelegate=None):
        """ Initialize the Tile Contents """
        self.imageBaseName = imageBaseName
        self.interactionDelegate = interactionDelegate
        if self.interactionDelegate is not None:
            self.interactionDelegate.setContent(self)
            
    def getImageBaseName(self):
        """ Return the image base name for the tile contents """
        return "Tiles/{0}.png".format(self.imageBaseName)
        
    def interact(self, direction):
        """ Interact with the contents """
        self.interactionDelegate.interact(direction)
        
    def setInteractionCallback(self, callback):
        """ Set the Person's Interaction Callback """
        self.interactionDelegate.callback = callback