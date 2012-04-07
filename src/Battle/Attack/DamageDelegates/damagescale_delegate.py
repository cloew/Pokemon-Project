from Battle.Actions.action_lock import ActionLock
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.EffectDelegates.multi_turn_delegate import MultiTurnDelegate

class DamageScaleDelegate(DamageDelegate, MultiTurnDelegate):
    """ Damage Delegate whose damage scales each turn it is used """
    
    def __init__(self, parent, power, isPhysical, factor, turns):
        """ """
        self.factor = factor
        DamageDelegate.__init__(self, parent, power, isPhysical)
        MultiTurnDelegate.__init__(self, turns, [])
        
    def coreDamage(self, user, target):
        """ Calculate the damage before modifiers and rands """
        scale = self.getScale()
        
        damage = super(DamageScaleDelegate, self).coreDamage(user, target)-2
        damage = damage*scale
        return damage + 2
        
    def getScale(self):
        """ Returns the scale based on the number of turns the attack has run """
        return self.factor**self.turnOn
        
    #def applyEffect(self, user, target):
    #    """ Applies the delegate's effect when the attack hits """
    #    if self.turnOn == 0:
    #        self.applyLock(user)
    #       
    #    self.incTurns()
    #   return []
        
    def effectOnMiss(self, user, target):
        """ Applies the delegate's effect on a miss """
        return self.stopCharge(user)
        
    def stopCharge(self, user):
        """ Stop Charge """
        self.turnOn = 0
        user.actionLock = None
        return []
        
    #def incTurns(self):
    #    """ Move to the next turn """
    #    self.turnOn = (self.turnOn+1)%self.turns
        
    #def applyLock(self, pkmn):
    #    """ Locks the side to use this move """
    #    pkmn.actionLock = ActionLock(pkmn,  \
    #                                                    pkmn.lastAction, self.turns-1)