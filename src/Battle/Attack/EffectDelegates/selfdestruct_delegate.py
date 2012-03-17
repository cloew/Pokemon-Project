from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SelfDestructDelegate(EffectDelegate):
    """ Represents a self-destruct effect on an Attack """
    message = " self-destructed."
    
    def __init__(self):
        """ Builds a self-destruct delegate """
        self.applyOnMiss = 1
        
    def applyEffect(self, user, target):
        """ Apply the recoil effect """
        messages = [user.getHeader() + SelfDestructDelegate.message]
        totake = user.getCurrHP()
        messages += user.takeDamage(totake)
        
        return messages