from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class PierceDodge2XDelegate(DamageDelegate):
    """ Represents an attack whose damage is doubled when used 
    against an opponent dodging in a certain manner """
    
    def __init__(self, parent, power, isPhysical, pierce):
        """ """
        self.parent = parent
        self.power = power
        self.isPhysical = isPhysical
        self.pierce = pierce
        
    def coreDamage(self, actingSide, otherSide):
        """ Doubles the damage when the opponent is dodging 
        in the manner that is pierced """
        damage = super(PierceDodge2XDelegate, self).coreDamage(actingSide, otherSide)
        if otherSide.dodge == self.pierce:
            return 2*damage
        else:
            return damage
            