import random


class ChanceDelegate:
    """ Represents an effect with a percent chance oif happening """
    
    def __init__(self, chance, effects):
        """ Builds a ChanceDelegate """
        self.chance = chance
        self.effects = effects
        
    def applyEffect(self, user, target):
        """ Applies the delegates effect """
        messages = []
        
        if self.shouldApply(random.randint(0,99)):
            for effect in self.effects:
                effectMessages = effect.applyEffect(user, target)
                messages = messages + effectMessages
                
        return messages
        
    def shouldApply(self, rand):
        """ Return if the effect should be applied """
        return rand < self.chance