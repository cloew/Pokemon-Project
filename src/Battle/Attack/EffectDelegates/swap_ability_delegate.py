from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwapAbilityDelegate(EffectDelegate):
    """ Effect that swaps abilities with target """
    message = "%s swapped abilities with %s."
    
    def applyEffect(self, user, target):
        """ Swap abilities with the target """
        userAbility = user.getAbility()
        targetAbility = target.getAbility()
        
        user.setAbility(targetAbility)
        target.setAbility(userAbility)
        
        return [self.message % (user.getHeader(), target.getHeader())]