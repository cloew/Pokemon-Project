from Battle.Actions.action_lock import ActionLock

class EncoreDelegate:
    """ Represents an attack that is locked for some number of future turns """
    
    def __init__(self, turns, affectUser):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.affectUser = affectUser
        
    def getTargetPkmn(self, user, target):
        """ Returns the Pkmn that is affected """
        if self.affectUser:
            return user
        else:
            return target
        
    def applyEffect(self, user, target):
        """ Applies the delegates effect """
        messages = []
        pkmn = self.getTargetPkmn(user, target)
        
        if not self.immune(pkmn):
            pkmn.encore = ActionLock(pkmn, pkmn.lastAction, self.turns)
                
        return messages
        
    def immune(self, pkmn):
        """ Returns if the target is immune to the attack """
        return not (pkmn.lastAction and hasattr(pkmn.lastAction, "attack") and not pkmn.encore)