from Battle.AfterTurnEffects.periodic_heal import PeriodicHeal

class PeriodicHealDelegate :
    """ Represents an effect that slowly heals the user """
    
    def __init__(self, startMessage, message):
        """ Build the Periodic Heal Delegate """
        self.startMessage = startMessage
        self.message = message
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the heal to the user """
        self.removePreviousHeal(actingSide)
        actingSide.afterEffects.append(PeriodicHeal(self.message))
        return [actingSide.getHeader() + self.startMessage]
        
    def removePreviousHeal(self, side):
        """ Checks if the side already has the heal """
        effect = self.hasHeal(side)
        if effect:
            side.afterEffects.remove(effect)
                
    def hasHeal(self, side):
        """ Returns if the side receiving the heal already has a heal """
        for effect in side.afterEffects:
            if isinstance(effect, PeriodicHeal):
                return effect
                
        return False 