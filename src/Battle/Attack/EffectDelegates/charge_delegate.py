from Battle.Actions.action_lock import ActionLock
from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class ChargeDelegate(EffectDelegate):
    """ Represents an attack that takes more than one turn to finish """
    
    def __init__(self, turns, turnToAttack, message):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.turnToAttack = turnToAttack
        self.message = message
        
        self.turnOn = 0
        
    def applyEffect(self, user, target):
        """ Applies the delegate's effect when the attack hits """
        return []
        
    def effectOnMiss(self, user, target):
        """ Applies the deleagte's effect on a miss """
        return self.stopCharge()
        
    def stopCharge(self, user):
        """ Stop Charge """
        self.turnOn = 0
        user.actionLock = None
        return []
        
    def isCharging(self, user):
        """ Modifies how the attack hits """
        # Check if the user is charging
        # AKA no damage should be calculated
        charging = True
        if self.turnToAttack == self.turnOn:
            charging = False
            
        # Check if this is the first turn
        # If so lock the move for its duration
        if self.turnOn == 0:
            self.applyLock(user)
            
        self.incTurn()
        return charging
        
    def incTurn(self):
        """ Move to the next turn """
        self.turnOn = (self.turnOn+1)%self.turns
        
    def applyLock(self, pkmn):
        """ Locks the pkmn to use this move """
        pkmn.actionLock = ActionLock(pkmn,  \
                                                        pkmn.lastAction, self.turns-1)