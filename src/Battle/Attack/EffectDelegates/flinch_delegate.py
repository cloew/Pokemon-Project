
class FlinchDelegate:
    """ Handles Flinch Effects """
    
    def applyEffect(self, actingSide, otherSide):
        """ Applies a flinch effect """
        otherSide.flinching = 1
        return []