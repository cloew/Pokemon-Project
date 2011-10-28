
class HealByRatioDelegate:
    """ Represents an effect that heals
    Abstract: Not to be instantiated """
    
    def __init__(self, healRatio):
        """ Build a HealDelegate by ratio """
        self.healRatio = healRatio
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the Delegates effect """
        self.heal(actingSide)
        return [actingSide.currPokemon.name + " restored some of its HP."]
        
    def heal(self, side):
        """ Heals the target """
        target = side.currPokemon
        toheal = self.damage/self.healRatio
        target.battleDelegate.heal(toheal)