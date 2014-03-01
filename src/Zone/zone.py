from Trainer.trainer_factory import TrainerFactory

from Zone.direction import UP, LEFT
from Zone.tile import Tile
from Zone.Person.person import Person
from Zone.Person.trainer_person import TrainerPerson
from Zone.Person.Interaction.interaction_delegate import InteractionDelegate

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
        for person in self.people:
            person.setInteractionCallback(callback)