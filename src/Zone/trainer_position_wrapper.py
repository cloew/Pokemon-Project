from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection

class TrainerPositionWrapper:
    """ Wrapper for a Trainer that includes it's position in a zone """
    
    def __init__(self, trainer, tile):
        """ Initialize the Trainer Position Wrapper """
        self.trainer = trainer
        self.tile = None
        self.setTile(tile)
        self.direction = DOWN
        
    def getImageBaseName(self):
        """ Return the base image name for the Trainer Position Wrapper """
        return "trainer_{0}".format(GetTextFromDirection(self.direction))
        
    def setTile(self, tile):
        """ Set the Trainer's current tile """
        if self.tile is not None:
            self.tile.setContents(None)
        self.tile = tile
        tile.setContents(self)
        
    def up(self):
        """ Move the Trainer up """
        self.tryToMove(UP)
        
    def down(self):
        """ Move the Trainer down """
        self.tryToMove(DOWN)
        
    def left(self):
        """ Move the Trainer left """
        self.tryToMove(LEFT)
        
    def right(self):
        """ Move the Trainer right """
        self.tryToMove(RIGHT)
        
    def tryToMove(self, direction):
        """ Try to Move in the given direction """
        if direction is not self.direction:
            self.direction = direction
        else:
            self.move(direction)
            
    def move(self, direction):
        """ Move in the given direction if possible """
        destination = self.getAdjacentTile(direction)
        if destination is not None:
            if destination.isEnterable():
                self.setTile(destination)
                
    def getAdjacentTile(self, direction):
        """ Returns the adjacent tile in the given direction """
        if direction in self.tile.connections:
            return self.tile.connections[direction]
        else:
            return None 