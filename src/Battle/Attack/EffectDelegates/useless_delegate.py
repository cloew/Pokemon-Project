from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class UselessDelegate(EffectDelegate):
    """ Effect that is completely useless"""
    message = "But nothing happened!"
    
    def applyEffect(self, user, target, environment):
        """ Apply Effect """
        return [self.message]