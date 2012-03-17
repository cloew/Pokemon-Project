from Battle.AfterTurnEffect.after_turn_effect import AfterTurnEffect

class SecondaryEffect(AfterTurnEffect):
    """ Represents a Secondary EFfect that is perpetuated """
    
    message = ""
    
    def immobilized(self, pkmn):
        """ Checks if the effect won't allow the attack to continue """
        return False, []
        
    def afterTurn(self, pkmn):
        """ Perform a between turns effect """
        return []