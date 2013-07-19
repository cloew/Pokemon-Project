from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection

class TrainerPositionWrapper:
    """ Wrapper for a Trainer that includes it's position in a zone """
    
    def __init__(self, trainer, tile):
        """ Initialize the Trainer Position Wrapper """
        self.trainer = trainer
        self.tile = tile
        self.direction = DOWN
        
    def getImageBaseName(self):
        """ Return the abse image name for the Trainer Position Wrapper """
        return "trainer_{0}".format(GetTextFromDirection(self.direction))
        
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
        if direction in self.tile.connections:
            self.tile = self.tile.connections[direction]