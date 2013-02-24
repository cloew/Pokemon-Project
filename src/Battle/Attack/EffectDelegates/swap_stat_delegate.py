from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwapStatDelegate(EffectDelegate):
    """ Effect that swaps stat values """
    message = "%s swapped its %s with its %s."
    
    def __init__(self, stat1, stat2):
        """ Builds an Effect with the specific stats """
        self.stat1 = stat1
        self.stat2 = stat2
    
    def applyEffect(self, user, target, environment):
        """ Swap abilities with the target """
        val1 = user.getStat(self.stat1)
        val2 = user.getStat(self.stat2)
        
        user.setStat(self.stat1, val2)
        user.setStat(self.stat2, val1)
        
        return [self.message % (user.getHeader(), self.stat1, self.stat2)]