from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class NullEffectDelegate(EffectDelegate):
    """ An empty Effect Delegate for attacks with no effect """
    
    def applyEffect(self, user, target, environment):
        return []
        