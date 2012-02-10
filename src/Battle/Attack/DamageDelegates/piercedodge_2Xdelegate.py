from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class PierceDodge2XDelegate(DamageDelegate):
    """ Represents an attack whose damage is doubled when used 
    against an opponent dodging in a certain manner """
    
    def __init__(self, parent, power, isPhysical, pierce):
        """ Build the Damage Delegate with the dodge it pierces """
        self.parent = parent
        self.power = power
        self.isPhysical = isPhysical
        self.pierce = pierce
        
    def coreDamage(self, user, target):
        """ Doubles the damage when the opponent is dodging 
        in the manner that is pierced """
        damage = super(PierceDodge2XDelegate, self).coreDamage(user, target)
        if target.dodge == self.pierce:
            return 2*damage
        else:
            return damage
            