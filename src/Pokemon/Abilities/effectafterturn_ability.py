from ability import Ability

class EffectAfterTurnAbility(Ability):
    """ An ability that prevents any crit """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        self.name = name
        self.effects = effects
        
    def afterTurn(self, user, target):
        """ Call the effects """
        messages = self.callEffects(user, target)
        return messages