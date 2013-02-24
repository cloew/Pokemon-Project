from ability import Ability

class EffectOnContactAbility(Ability):
    """ An ability that performs an effect when an 
    attack thta requires contact hits the owner """
    
    def __init__(self, name, effects):
        """ Builds the Ability """
        Ability.__init__(self)
        self.name = name
        self.effects = effects
        
    def onContact(self, receiver, attacker):
        """ Perform an effect when a stat is modded """
        messages = self.callEffects(user=receiver, target=attacker)
        return messages