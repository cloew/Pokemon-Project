from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate

class CritModDelegate(StatModDelegate):
    """ Represents an effect that increases crit chance """
    message = "It's pumped."
    
    def __init__(self, degree):
        """ Build the Delegate with the constants for CritMod
              Stat is always CRT | Always affects user """
        StatModDelegate.__init__(self, "CRT", degree, 1)
    
    def applyEffect(self, user, target, environment):
        """ Applies the delegates effect """
        self.applyMod(user)
        return [CritModDelegate.message]