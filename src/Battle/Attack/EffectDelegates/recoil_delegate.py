
class RecoilDelegate:
    """ Represents a recoil effect on an Attack """
    message = " was hit by recoil."
    
    def __init__(self, recoilRatio):
        """ Builds a Recoil Effect with a set ration """
        self.recoilRatio = recoilRatio      # The percentage of the damage to do as recoil
        
    def setDamage(self, damage):
        """ Set the damage that the recoil will be based on """
        self.damage = damage
        
    def applyEffect(self, user, target):
        """ Apply the recoil effect """
        messages = [user.getHeader() + RecoilDelegate.message]
        
        totake = self.damage/self.recoilRatio
        totake = self.normalize(totake)
        messages += user.takeDamage(totake)
        
        return messages
        
    def normalize(self, damage):
        if damage < 1:
            return 1
        else:
            return int(damage)