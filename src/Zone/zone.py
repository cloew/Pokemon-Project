from Trainer.trainer_factory import TrainerFactory

from Zone.direction import UP, LEFT
from Zone.tile import Tile
from Zone.Person.person import Person
from Zone.Person.trainer_person import TrainerPerson

class Zone:
    """ Represents a Zone in the Game """
    
    def __init__(self):
        """ Initialize the Zone """
        self.tiles = []
        
        rows = 5
        columns = 20
        
        for i in range(rows):
            row = []
            for j in range(columns):
                tile = Tile()
                if j > 0:
                    tile.connectToTile(row[j-1], LEFT)
                if i > 0:
                    tile.connectToTile(self.tiles[i-1][j], UP)
                row.append(tile)
            self.tiles.append(row)
            
        self.enemyTrainer = TrainerPerson(self.tiles[rows-2][columns/2], TrainerFactory.loadFromXML("Badass", "Eric", TrainerFactory.COMPUTER))
        self.npc = Person(self.tiles[rows-3][columns/2-2])