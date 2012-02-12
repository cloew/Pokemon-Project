
class HealByRatioDelegate:
    """ Represents an effect that heals
    Abstract: Not to be instantiated """
    message = " restored some of its HP."
    
    def __init__(self, healRatio):
        """ Build a HealDelegate by ratio """
        self.healRatio = healRatio
        
    def applyEffect(self, user, target):
        """ Applies the Delegates effect """
        self.heal(user)
        return [user.getHeader() + HealByRatioDelegate.message]
        
    def heal(self, pkmn):
        """ Should be overwritten in sub class to heal the given pkmn """