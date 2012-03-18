from ability import Ability

class EffectAfterTurnAbility(Ability):
    """ An ability that prevents any crit """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        super(EffectAfterTurnAbility, self).__init__()
        self.name = name
        self.effects = effects
        
    def afterTurn(self, pkmn):
        """ Call the effects """
        messages = self.callEffects(pkmn)
        return messages