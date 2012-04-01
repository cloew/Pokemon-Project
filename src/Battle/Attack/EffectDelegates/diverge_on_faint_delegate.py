from Battle.Attack.EffectDelegates.diverge_delegate import DivergeDelegate

class DivergeOnFaintDelegate(DivergeDelegate):
    """ An Effect that acts differnetly if the target has fainted """
        
    def diverge(self, user, target):
        """ Function to determine if the diverge effects should be called
        Should be overridden in sub classes """
        return target.fainted()