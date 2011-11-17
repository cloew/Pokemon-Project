
class SecondaryEffect:
    """ Represents a Secondary EFfect that is perpetuated """
    
    message = ""
    
    def immobilized(self, side):
        """ Checks if the effect won't allow the attack to continue """
        return False, []
        
    def afterTurn(self, side):
        """ Perform a between turns effect """
        return []