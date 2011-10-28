from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class HalfHealthDelegate(DamageDelegate):
    """ Does damage equivalent to half the target's current health """
    
    def __init__(self, parent, isPhysical):
        """ Build the Delegate """
        self.parent = parent
        self.isPhysical = isPhysical
    
    def calcDamage(self, actingSide, otherSide):
        """ Returns damage as half the target's health """
        return otherSide.currPokemon.battleDelegate.currHP/2