from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class FixedDelegate(DamageDelegate):
    """ Deals damage based on level """
    def __init__(self, parent, damage, physical):
        """ Set physical """
        self.parent = parent
        self.fixedDamage = damage
        self.physical = physical
        
    def calcDamage(self, actingSide, otherSide):
        """ Return the level of the user """
        return self.fixedDamage