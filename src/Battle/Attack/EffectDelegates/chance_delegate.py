from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

import random

class ChanceDelegate(EffectDelegate):
    """ Represents an effect with a percent chance oif happening """
    
    def __init__(self, chance, effects):
        """ Builds a ChanceDelegate """
        self.chance = chance
        self.effects = effects
        
    def applyEffect(self, user, target, environment):
        """ Applies the delegates effect """
        messages = []
        
        if self.shouldApply(random.randint(0,99)):
            messages += self.performEffects(self.effects, user, target, environment)
                
        return messages
        
    def shouldApply(self, rand):
        """ Return if the effect should be applied """
        return rand < self.chance