from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class DivergeOnFaintDelegate(EffectDelegate):
    """ An Effect that acts differnetly if the target has fainted """
    
    def __init__(self, effectsOnFaint, effectsNoFaint):
        """ Build the Diverge On Faint Effect """
        self.effectsOnFaint = effectsOnFaint
        sel.feffectsNoFaint = effectsNoFaint
    
    def applyEffect(self, user, target):
        """ Apply Effect """
        messages = []
        
        if target.fainted():
            messages += self.doEffects(self.effectsOnFaint, user, target)
        else:
            messages += self.doEffects(self.effectsNoFaint, user, target)
        
        return messages
        
    def performEffects(self, effects, user, target):
        """ Perform the effects given """
        mesasges = []
        for effect in effects:
            messages += effects.tryToApplyEffect(user, target)
        return messages