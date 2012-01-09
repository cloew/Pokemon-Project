from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

import random

class StatusHitDelegate(HitDelegate):
    """ Represents an Attack's ability to hit an opponent """
    accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 9,
                    1/3.0, 3/8.0, .428, 1/2.0, 3/5.0, 3/4.0]
  
    message = "But it failed."
  
    def __init__(self, parent, toHit):
        """ Build a core hit Delegate """
        self.parent = parent
        self.chanceToHit = toHit
    
    
    def hit(self, user, target):
        """ Returns whether or not an attack hit its target """
        if self.immune(user, target):
            return False, [self.message]
        
        return super(StatusHitDelegate, self).hit(user, target)
        
        
    def immune(self, user, target):
        """ Check if the target is immune to the effect """
        immune = False
        
        for effect in self.parent.effectDelegates:
            if hasattr(effect, "immune") and effect.immune(user, target):
                immune = True
            else:
                return False
                    
        return immune