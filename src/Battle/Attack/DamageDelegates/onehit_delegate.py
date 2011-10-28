from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class OneHitDelegate(DamageDelegate):
    """ Handles One Hit KOs """
    def __init__(self, parent, isPhysical):
        """ Initialize with a physical """
        self.parent = parent
        self.isPhysical = isPhysical
    
    def damage(self, actingSide, otherSide):
        """ Deals damage for a One Hit KO """
        target = otherSide.currPokemon
        
        messages = []
        
        mod = self.getEffectiveness(messages, target)
        
        if mod is 0:
            return messages
            
        damage = target.battleDelegate.currHP
        self.takeDamage(damage, target)
        
        return ["One-hit KO"]