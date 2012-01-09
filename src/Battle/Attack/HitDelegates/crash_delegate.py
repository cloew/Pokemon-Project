from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

import random

class CrashDelegate(HitDelegate):
    """ An attack that can crash if it misses """
    
    def __init__(self, parent, toHit, recoilEffect):
        """ Build a crash delegate """
        self.parent = parent
        self.chanceToHit = toHit
        self.recoilEffect = recoilEffect
        
    def hit(self, user, target):
        """ Calculates if the attack hits or misses
        If it misses"""
        hit, messages = super(CrashDelegate, self).hit(user, target)
        
        if hit:
            return True, []
        else:
            self.crash(user, target)
            return False, [self.message, user.currPokemon.name + " kept going and crashed."]
        
    def crash(self, user, target):
        """ Apply damage from crashing """
        damage, messages = self.parent.damageDelegate.damage(user, target)
        
        self.recoilEffect.setDamage(damage)
        self.recoilEffect.applyEffect(user, target)