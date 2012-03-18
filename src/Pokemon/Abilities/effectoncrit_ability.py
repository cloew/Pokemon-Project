from ability import Ability

class EffectOnCritAbility(Ability):
    """ An ability that performs effects when taking a crit """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        super(EffectOnCritAbility, self).__init__()
        self.name = name
        self.effects = effects
        
    def takeCrit(self, critMod, thisSide, otherSide):
        """ Prevent the crit """
        messages = self.callEffects(thisSide, otherSide)
        return critMod, messages