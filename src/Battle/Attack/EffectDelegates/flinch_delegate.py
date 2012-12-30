from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class FlinchDelegate(EffectDelegate):
    """ Handles Flinch Effects """
    
    def applyEffect(self, user, target, environment):
        """ Applies a flinch effect """
        target.flinching = 1
        return []