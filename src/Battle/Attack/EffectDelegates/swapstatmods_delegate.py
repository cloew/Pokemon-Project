from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwapStatModsDelegate(EffectDelegate):
    """ Effect that swaps stat boosts between sides """
    message = " switched stat changes with the target!"
    
    def applyEffect(self, user, target):
        """ Applies the delegate's effect when the attack hits """
        temp = target.statMods
        target.statMods = user.statMods
        user.statMods = temp
        return [user.getHeader() + SwapStatModsDelegate.message]