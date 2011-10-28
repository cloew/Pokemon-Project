import random


class ChanceDelegate:
    """ Represents an effect with a percent chance oif happening """
    
    def __init__(self, chance, effects):
        """ Builds a ChanceDelegate """
        self.chance = chance
        self.effects = effects
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegates effect """
        messages = []
        
        if random.randint(0,99) < self.chance:
            for effect in self.effects:
                effectMessages = effect.applyEffect(actingSide, otherSide)
                messages = messages + effectMessages
                
        return messages
            