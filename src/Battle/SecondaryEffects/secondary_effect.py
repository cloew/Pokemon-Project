from Battle.AfterTurnEffect.after_turn_effect import AfterTurnEffect

class SecondaryEffect(AfterTurnEffect):
    """ Represents a Secondary EFfect that is perpetuated """
    
    message = "The mist prevents %s's stats from lowering."
    
    def immobilized(self, owner):
        """ Checks if the effect won't allow the attack to continue """
        return False, []
        
    def afterTurn(self, owner):
        """ Perform a between turns effect """
        return []
        
    def onStatMod(self, owner, degree, messages):
        """ Perform effect when owner is given a stat mod """
        return degree