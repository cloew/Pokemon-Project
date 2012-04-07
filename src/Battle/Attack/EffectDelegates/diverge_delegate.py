from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class DivergeDelegate(EffectDelegate):
    """ An Effect whose effects diverge on a specific condition """
    
    def __init__(self, effectsOnDiverge, effectsNormal):
        """ Build the Diverge Effect """
        self.effectsOnDiverge = effectsOnDiverge
        self.effectsNormal = effectsNormal
    
    def applyEffect(self, user, target):
        """ Apply Effect """
        messages = []
        
        if self.diverge(user, target):
            messages += self.performEffects(self.effectsOnDiverge, user, target)
        else:
            messages += self.performEffects(self.effectsNormal, user, target)
        
        return messages
        
    def diverge(self, user, target):
        """ Function to determine if the diverge effects should be called
        Should be overridden in sub classes """
        return self.diverging
        