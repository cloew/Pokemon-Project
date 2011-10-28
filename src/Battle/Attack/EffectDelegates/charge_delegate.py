from Battle.Actions.action_lock import ActionLock

class ChargeDelegate(object):
    """ Represents an attack that takes more than one turn to finish """
    
    def __init__(self, turns, turnToAttack, message):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.turnToAttack = turnToAttack
        self.message = message
        
        self.turnOn = 0
        
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegate's effect when the attack hits """
        return []
        
    def effectOnMiss(self, actingSide, otherSide):
        """ Applies the deleagte's effect on a miss """
        self.turnOn = 0
        actingSide.trainer.actionLock = None
        return []
        
    def isCharging(self, actingSide):
        """ Modifies how the attack hits """
        # Check if the user is charging
        # AKA no damage should be calculated
        charging = True
        if self.turnToAttack == self.turnOn:
            charging = False
            
        # Check if this is the first turn
        # If so lock the move for its duration
        if self.turnOn == 0:
            self.applyLock(actingSide)
            
        self.incTurn()
        return charging
        
    def incTurn(self):
        """ Move to the next turn """
        self.turnOn = (self.turnOn+1)%self.turns
        
    def applyLock(self, side):
        """ Locks the side to use this move """
        side.trainer.actionLock = ActionLock(side.trainer,  \
                                                        side.lastAction, self.turns-1)