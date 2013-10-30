from Trainer.trainer_factory import TrainerFactory

from Zone.direction import UP, LEFT
from Zone.tile import Tile
from Zone.Person.person import Person
from Zone.Person.trainer_person import TrainerPerson
from Zone.Person.Interaction.interaction_delegate import InteractionDelegate

class Zone:
    """ Represents a Zone in the Game """
    
    def __init__(self, rows, columns, callback=None):
        """ Initialize the Zone """
        self.tiles = []
        
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
            
        self.enemyTrainer = TrainerPerson(self.tiles[2][2], "trainer2", TrainerFactory.loadFromXML("Badass", "Eric", TrainerFactory.COMPUTER), InteractionDelegate("Hi! I'm Eric! Let's battle!", callback))
        self.npc = Person(self.tiles[1][2], "npc", InteractionDelegate("Hi! I'm an NPC! I'm like a platypus. They don't do much you know.", callback))