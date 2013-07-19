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