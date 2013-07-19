from Zone.direction import UP, DOWN, LEFT, RIGHT, GetTextFromDirection, GetOppositeDirection
from Zone.Person.person import Person

class TrainerPerson(Person):
    """ A person that also acts as a trainer """
    
    def __init__(self, tile, imageBaseName, trainer, interactionCallback=None, message=None):
        """ Initialize the Trainer Position Wrapper """
        self.trainer = trainer
        Person.__init__(self, tile, imageBaseName, interactionCallback, message)
            
    def isBattleable(self):
        """ Return if the trainer is Battleable """
        return self.trainer.hasPokemon()