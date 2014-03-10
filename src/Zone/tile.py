from Zone.direction import GetOppositeDirection

class Tile:
    """ Represents a tile in a Pokemon Zone """
    
    def __init__(self, row, column, tileFilename):
        """ Initialize the Zone Tile """
        self.row = row
        self.column = column
        self.tileFilename = tileFilename
        self.connections = {}
        self.contents = None
        self.enterDelegate = None
        
    def connectToTile(self, tile, direction, twoWay=True):
        """ Connect this tile and the given tile """
        self.connections[direction] = tile
        
        if twoWay:
            tile.connectToTile(self, GetOppositeDirection(direction), twoWay=False)
            
    def isEnterable(self):
        """ Return if the tile can be entered """
        return self.contents is None
        
    def onEnter(self):
        """ Perform enter event """
        if self.enterDelegate is not None:
            self.enterDelegate.onEnter()
            
    def setContents(self, contents):
        """ Sets the tile's contents """
        self.contents = contents