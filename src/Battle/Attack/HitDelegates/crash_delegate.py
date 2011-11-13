from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

import random

class CrashDelegate(HitDelegate):
    """ An attack that can crash if it misses """
    
    def __init__(self, parent, toHit, recoilEffect):
        """ Build a crash delegate """
        self.parent = parent
        self.chanceToHit = toHit
        self.recoilEffect = recoilEffect
        
    def hit(self, actingSide, otherSide):
        """ Calculates if the attack hits or misses
        If it misses"""
        hit, messages = super(CrashDelegate, self).hit(actingSide, otherSide)
        
        if hit:
            return True, []
        else:
            self.crash(actingSide, otherSide)
            return False, [self.message, actingSide.currPokemon.name + " kept going and crashed."]
        
    def crash(self, actingSide, otherSide):
        """ Apply damage from crashing """
        damage, messages = self.parent.damageDelegate.damage(actingSide, otherSide)
        
        self.recoilEffect.setDamage(damage)
        self.recoilEffect.applyEffect(actingSide, otherSide)