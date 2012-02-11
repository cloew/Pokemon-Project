from Battle.Actions.action_lock import ActionLock

class ApplyLockDelegate:
    """ Represents an attack that is locked for some number of future turns """
    
    def __init__(self, turns, affectUser):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.affectUser = affectUser
        
    def applyEffect(self, user, target):
        """ Applies the delegates effect """
        if self.affectUser:
            return self.affectPkmn(user)
        else:
            return self.affectPkmn(target)
        
    def affectPkmn(self, pkmn):
        """ Applies the lock to the correct pkmn """
        message = []
        if pkmn.lastAction and hasattr(pkmn.lastAction, "attack"):
            pkmn.actionLock = ActionLock(pkmn,  \
                                                        pkmn.lastAction, self.turns)
        else:
            message = ["But it failed"]
                
        return message