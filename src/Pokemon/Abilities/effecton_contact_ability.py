from ability import Ability

class EffectOnContactAbility(Ability):
    """ An ability that performs an effect when an 
    attack thta requires contact hits the owner """
    
    def __init__(self, name, effects, message):
        """ Builds the Ability """
        Ability.__init__(self)
        self.name = name
        self.effects = effects
        self.message = message
        
    def onContact(self, pkmn, attacker):
        """ Perform an effect when a stat is modded """
        messages = self.callEffects(pkmn)
        return messages