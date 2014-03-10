from Zone.direction import GetOppositeDirection
from Zone.Entry.teleport_entry_delegate import TeleportEntryDelegate

class Tile:
    """ Represents a tile in a Pokemon Zone """
    
    def __init__(self, row, column, tileFilename):
        """ Initialize the Zone Tile """
        self.row = row
        self.column = column
        self.tileFilename = tileFilename
        self.connections = {}
        
        self.contents = None
        self.entryDelegate = None
        # if self.row == 0 and self.column == 9:
            # self.enterDelegate = TeleportEntryDelegate()
        
    def connectToTile(self, tile, direction, twoWay=True):
        """ Connect this tile and the given tile """
        self.connections[direction] = tile
        
        if twoWay:
            tile.connectToTile(self, GetOppositeDirection(direction), twoWay=False)
            
    def isEnterable(self):
        """ Return if the tile can be entered """
        return self.contents is None
        
    def onEnter(self, player):
        """ Perform enter event """
        if self.entryDelegate is not None:
            self.entryDelegate.onEnter(player)
            
    def setContents(self, contents):
        """ Sets the tile's contents """
        self.contents = contents
        
    def setCallbacks(self, callback):
        """ Set the callback for tile based events """
        if self.contents is not None:
            self.contents.setInteractionCallback(callback)
            
        if self.entryDelegate is not None:
            self.entryDelegate.setCallback(callback)