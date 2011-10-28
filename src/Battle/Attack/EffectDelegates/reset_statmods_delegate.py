
class ResetStatmodsDelegate:
    """ Resets all the Stat modifiers for both sides """
    
    def applyEffect(self, actingSide, otherSide):
        """ Tells both sides to reset their stat mods """
        actingSide.resetStatMods()
        otherSide.resetStatMods()
        return ["Everything returned to normal."]