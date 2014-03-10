from Trainer.trainer_factory import TrainerFactory

from Zone.direction import UP, LEFT
from Zone.tile import Tile

class Zone:
    """ Represents a Zone in the Game """
    
    def __init__(self, rows, columns, tileFilename):
        """ Initialize the Zone """
        self.people = []
        self.tiles = []
        self.tileFilename = tileFilename
        
        for i in range(rows):
            row = []
            for j in range(columns):
                tile = Tile(i, j, tileFilename)
                if j > 0:
                    tile.connectToTile(row[j-1], LEFT)
                if i > 0:
                    tile.connectToTile(self.tiles[i-1][j], UP)
                row.append(tile)
            self.tiles.append(row)
            
    def setCallbacks(self, callback):
        """ Set Callbacks to allow each Person in the Zone 
            to interact with the Window to display messages """
        for row in self.tiles:
            for tile in row:
                tile.setCallbacks(callback)
        # contents = []
        # for row in self.tiles:
            # contents += [tile.contents for tile in row if tile.contents is not None]
        
        # for content in contents:
            # content.setInteractionCallback(callback)