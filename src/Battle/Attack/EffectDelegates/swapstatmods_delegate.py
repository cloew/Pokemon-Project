
class SwapStatModsDelegate:
    """ Effect that swaps stat boosts between sides """
    
    def applyEffect(self, user, target):
        """ Applies the delegate's effect when the attack hits """
        temp = target.statMods
        target.statMods = user.statMods
        user.statMods = temp
        return [user.pkmn.name + " switched stat changes with the target!"]