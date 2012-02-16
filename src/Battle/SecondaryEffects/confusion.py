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
        
    def immobilized(self, user):
        """ Checks if the confusion prevents the current attack """
        messages = []
        immobilized = False
        
        if self.checkOver(user, messages):
            immobilized = False
        
        elif self.confused(random.randint(0, 1)):
            self.doDamage(user, messages)
            immobilized = True
            
        return immobilized, messages
        
    def checkOver(self, user, messages):
        """ Check if the Confusion is cured """
        over = self.turns == 0
        
        if over:
            self.cure(user)
            messages.append(user.getHeader() + self.over)
        else:
            self.turns -= 1
            messages.append(user.getHeader() + self.start)
        return over
            
    def cure(self, user):
        """ Cure the confusion """
        user.secondaryEffects.remove(self)
        
    def confused(self, rand):
        """ Return wether the Pkmn should hurt itself in its confusion """
        return rand > 0
        
    def doDamage(self, user, messages):
        """ Do Damage to the confused user """
        self.damageDelegate.doDamage(user, user)
        messages.append(self.hurtItself)