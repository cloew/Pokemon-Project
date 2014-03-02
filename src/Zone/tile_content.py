
class TileContent:
    """ Represents content in a tile """
    
    def __init__(self, imageBaseName):
        """ Initialize the Tile Contents """
        self.imageBaseName = imageBaseName
    
    def getImageBaseName(self):
        """ Return the image base name for the tile contents """
        return "Tiles/{0}.png".format(self.imageBaseName)
        
    def interact(self, direction):
        """ Interact with the contents """