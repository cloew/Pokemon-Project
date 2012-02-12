
class SelfDestructDelegate:
    """ Represents a self-destruct effect on an Attack """
    message = " self-destructed."
    
    def __init__(self):
        """ Builds a self-destruct delegate """
        self.applyOnMiss = 1
        
    def applyEffect(self, user, target):
        """ Apply the recoil effect """
        totake = user.getCurrHP()
        user.takeDamage(totake)
        
        return [user.getHeader() + SelfDestructDelegate.message]