
class FlinchDelegate:
    """ Handles Flinch Effects """
    
    def applyEffect(self, user, target):
        """ Applies a flinch effect """
        target.flinching = 1
        return []