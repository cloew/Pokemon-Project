

class AfterTurnEffect:
    """ Represents any Effect with the capability to occur after a turn """
    message = ""
    
    def attemptAfterTurn(self, pkmn):
        """ Applies After Turn Effect unless the pkmn that owns the effect has fainted """
        if pkmn.fainted():
            return []
            
        return self.afterTurn(pkmn)
        
    def afterTurn(self, pkmn):
        """ Applies the After Turn Effect -- SHould be overriden in subclasses """
        return [AfterTurnEffect.message]