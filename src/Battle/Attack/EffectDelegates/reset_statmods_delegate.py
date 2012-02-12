
class ResetStatModsDelegate:
    """ Resets all the Stat modifiers for both sides """
    message = "Everything returned to normal."
    
    def applyEffect(self, actingSide, otherSide):
        """ Tells both sides to reset their stat mods """
        actingSide.resetStatMods()
        otherSide.resetStatMods()
        return [ResetStatModsDelegate.message]