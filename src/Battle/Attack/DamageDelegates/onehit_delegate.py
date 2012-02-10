from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class OneHitDelegate(DamageDelegate):
    """ Handles One Hit KOs """
    message = "One-hit KO"
    
    def __init__(self, parent, isPhysical):
        """ Initialize with a physical """
        self.parent = parent
        self.isPhysical = isPhysical
    
    def damage(self, user, target):
        """ Deals damage for a One Hit KO """
        messages = []
        
        mod = self.getEffectiveness(messages, target)
        
        if mod is 0:
            return 0, messages
            
        damage = target.getCurrHP()
        return damage, [OneHitDelegate.message]