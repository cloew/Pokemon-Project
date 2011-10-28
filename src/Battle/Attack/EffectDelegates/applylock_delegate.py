from Battle.Actions.action_lock import ActionLock

class ApplyLockDelegate:
    """ Represents an attack that is locked for some number of future turns """
    
    def __init__(self, turns, affectUser):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.affectUser = affectUser
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegates effect """
        if self.affectUser:
            return self.affectSide(actingSide)
        else:
            return self.affectSide(otherSide)
        
    def affectSide(self, side):
        """ Applies the lock to the correct side """
        message = []
        if side.lastAction and hasattr(side.lastAction, "attack"):
            side.trainer.actionLock = ActionLock(side.trainer,  \
                                                        side.lastAction, self.turns)
        else:
            message = ["But it failed"]
                
        return message