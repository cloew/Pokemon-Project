from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class DivergeOnFaintDelegate(EffectDelegate):
    """ An Effect that acts differnetly if the target has fainted """
    
    def __init__(self, effectsOnFaint, effectsNoFaint):
        """ Build the Diverge On Faint Effect """
        self.effectsOnFaint = effectsOnFaint
        self.effectsNoFaint = effectsNoFaint
    
    def applyEffect(self, user, target):
        """ Apply Effect """
        messages = []
        
        if target.fainted():
            messages += self.performEffects(self.effectsOnFaint, user, target)
        else:
            messages += self.performEffects(self.effectsNoFaint, user, target)
        
        return messages
        
    def performEffects(self, effects, user, target):
        """ Perform the effects given """
        messages = []
        for effect in effects:
            messages += effect.tryToApplyEffect(user, target)
        return messages