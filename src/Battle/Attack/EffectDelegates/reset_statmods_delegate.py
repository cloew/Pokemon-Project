from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class ResetStatModsDelegate(EffectDelegate):
    """ Resets all the Stat modifiers for both sides """
    message = "Everything returned to normal."
    
    def applyEffect(self, user, target, environment):
        """ Tells both sides to reset their stat mods """
        user.resetStatMods()
        target.resetStatMods()
        return [ResetStatModsDelegate.message]