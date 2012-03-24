from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class NoFaintDelegate(DamageDelegate):
    """ Damage Delegate that will never cause the Target to faint """
    
    def normalize(self, damage, target):
        """ Normalize damage so it is never enough to knock out the target """
        damage = super(NoFaintDelegate, self).normalize(damage, target)
        if damage >= target.getCurrHP():
            damage = target.getCurrHP() - 1
            
        return damage