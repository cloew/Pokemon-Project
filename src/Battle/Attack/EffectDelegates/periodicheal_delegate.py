from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate
from Battle.SecondaryEffects.periodic_heal import PeriodicHeal

class PeriodicHealDelegate(EffectDelegate):
    """ Represents an effect that slowly heals the user """
    
    def __init__(self, startMessage, message):
        """ Build the Periodic Heal Delegate """
        self.startMessage = startMessage
        self.message = message
        
    def applyEffect(self, user, target):
        """ Apply the heal to the user """
        self.removePreviousHeal(user)
        user.secondaryEffects.append(PeriodicHeal(self.message))
        return [user.getHeader() + self.startMessage]
        
    def removePreviousHeal(self, pkmn):
        """ Checks if the pkmn already has the heal """
        effect = self.hasHeal(pkmn)
        if effect:
            pkmn.secondaryEffects.remove(effect)
                
    def hasHeal(self, pkmn):
        """ Returns if the pkmn receiving the heal already has a heal """
        for effect in pkmn.secondaryEffects:
            if isinstance(effect, PeriodicHeal):
                return effect
                
        return False 