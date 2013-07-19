from Zone.tile import Tile

class Zone:
    """ Represents a Zone in the Game """
    
    def __init__(self):
        """ Initialize the Zone """
        self.tiles = []
        
        for i in range(20):
            row = []
            for j in range(20):
                row.append(Tile())
            self.tiles.append(row)