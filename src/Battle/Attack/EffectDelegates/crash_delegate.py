from Battle.Attack.EffectDelegates.recoil_delegate import RecoilDelegate

class CrashDelegate(RecoilDelegate):
    """ Represents an effect with recoil when the attack misses """
    message = "%s kept going and crashed."
    
    def __init__(self, parent, recoilRatio):
        """ Builds a Recoil Effect with a set ration """
        self.parent = parent
        RecoilDelegate.__init__(self, recoilRatio, preventable=False)
        
    def applyEffect(self, user, target, environment):
        """ No effect normally"""
        return []
        
    def effectOnMiss(self, user, target, environment):
        """ Applies the Recoil on Miss """
        self.damage, messages = self.parent.damageDelegate.damage(user, target)
        return RecoilDelegate.applyEffect(self, user, target, environment)