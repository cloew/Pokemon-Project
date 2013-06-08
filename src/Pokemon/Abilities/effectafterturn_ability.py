from ability import Ability

class EffectAfterTurnAbility(Ability):
    """ An ability that performs an effect after turn """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        super(EffectAfterTurnAbility, self).__init__(name)
        self.effects = effects
        
    def afterTurn(self, pkmn):
        """ Call the effects """
        messages = self.callEffects(user=pkmn)
        return messages