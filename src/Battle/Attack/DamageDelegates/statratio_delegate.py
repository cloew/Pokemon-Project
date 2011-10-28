from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class StatRatioDelegate(DamageDelegate):
    """ Represents an attack whose damage is based as the ratio of two stats """
    max = 150
    base = 25
    
    def __init__(self, parent, isPhysical, stat):
        """ Builds the StatRatioDelegate """
        self.parent = parent
        self.isPhysical = isPhysical
        self.stat = stat
        
    def getPower(self, actingSide, otherSide):
        """ Returns the power of the move based on the ratio of the stat """
        ratio = self.getStatWithMod(self.stat, otherSide)/self.getStatWithMod(self.stat, actingSide)
        power = StatRatioDelegate.base*ratio
        if power > StatRatioDelegate.max:
            power = StatRatioDelegate.max
        return power