from ability import Ability

class EffectOnStatModAbility(Ability):
    """ An ability that performs an effect on stat mod """
    
    def __init__(self, name, effects, message):
        """ Builds the Ability """
        super(EffectOnStatModAbility, self).__init__(name)
        self.effects = effects
        self.message = message
        
    def onStatMod(self, pkmn, stat, degree, selfInflicted):
        """ Perform when a stat is modded """
        messages = []
        if not selfInflicted:
            self.callEffects(user=pkmn)
            messages.append(self.message % pkmn.getHeader())
            
        return degree, messages #  Returns a modified degree and any messages related to that