from ability import Ability

class EffectAfterTurnAbility(Ability):
    """ An ability that prevents any crit """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        self.name = name
        self.effects = effects
        
    def afterTurn(self, thisSide, otherSide):
        """ Prevent the crit """
        messages = self.callEffects(thisSide, otherSide)
        return messages