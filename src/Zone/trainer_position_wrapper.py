
class TrainerPositionWrapper:
    """ Wrapper for a Trainer that includes it's position in a zone """
    
    def __init__(self, trainer, tile):
        """ Initialize the Trainer Position Wrapper """
        self.trainer = trainer
        self.tile = tile
        