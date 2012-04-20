from Battle.Attack.EffectDelegates.diverge_delegate import DivergeDelegate

class DivergeOnFirstTurnDelegate(DivergeDelegate):
    """ An Effect that acts differently if the user has not used a an action yet """
        
    def diverge(self, user, target):
        """ Function to determine if the diverge effects should be called
        Should be overridden in sub classes """
        return user.lastAction is None
        