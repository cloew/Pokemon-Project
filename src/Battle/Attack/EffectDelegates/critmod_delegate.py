from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate

class CritModDelegate(StatModDelegate):
    """ Represents an effect that increases crit """
    
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegates effect """
        self.applyMod(actingSide)
        return ["It's pumped."]