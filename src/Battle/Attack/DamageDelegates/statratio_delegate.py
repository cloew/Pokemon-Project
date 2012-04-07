from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class StatRatioDelegate(DamageDelegate):
    """ Represents an attack whose damage is based as the ratio of two stats """
    
    def __init__(self, parent, isPhysical, stat):
        """ Builds the StatRatioDelegate """
        self.parent = parent
        self.isPhysical = isPhysical
        self.stat = stat
        
    def getStatRatio(self, user, target):
        """ Returns the ratio of the stats """
        return self.getStatWithMod(self.stat, target)/self.getStatWithMod(self.stat, user)