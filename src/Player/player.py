
class Player:
    """ Represents a player in the Pokemon Game """
    
    def __init__(self, trainer, zone, row, column):
        """ Initialize the Player """
        self.trainer = trainer
        self.zone = zone
        self.row = row
        self.column = column
        
    @property
    def fullname(self):
        """ Return the fullname of the Player """
        return "{0} {1}".format(self.trainer.title, self.trainer.name)