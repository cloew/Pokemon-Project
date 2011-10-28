
class SwapStatModsDelegate:
    """ Effect that swaps stat boosts between sides """
    
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegate's effect when the attack hits """
        temp = otherSide.statMods
        otherSide.statMods = actingSide.statMods
        actingSide.statMods = temp
        return [actingSide.currPokemon.name + " switched stat changes with the target!"]