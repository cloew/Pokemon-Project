from secondary_effect import SecondaryEffect

from Battle.Attack.DamageDelegates.damage_delegatefactory import DamageDelegateFactory

import random

class Confusion(SecondaryEffect):
    """ Represents a Pokemon having the status of confusion """
    
    damageDelegate = DamageDelegateFactory.getConfusionAttack()
    min = 2
    max = 4
    
    start = " is confused."
    hurtItself = "It hurt itself in its confusion."
    already = " is already confused."
    over = " is no longer confused."
    
    def __init__(self):
        self.turns = self.getTurns()
        
    def getTurns(self):
        """ Returns a # of turns from 1-7 """
        return random.randint(self.min, self.max)
        
    def immobilized(self, side):
        """ Checks if the confusion prevents the current attack """
        if self.turns == 0:
            side.secondaryEffects.remove(self)
            return False, [side.getHeader() + self.over]
            
        self.turns = self.turns -1
        messages = [side.getHeader() + self.start]
        
        if random.randint(0,1) > 0:
            self.damageDelegate.doDamage(side, side)
            return True, messages + [self.hurtItself]
        return False, messages