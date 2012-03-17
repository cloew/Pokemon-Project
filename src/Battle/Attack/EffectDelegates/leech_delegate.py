from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate
from Battle.SecondaryEffects.leech import Leech

class LeechDelegate(EffectDelegate):
    """ Represents an effect that slowly heals the user """
    
    def __init__(self, startMessage, message, type):
        """ Build the Leech Delegate """
        self.startMessage = startMessage
        self.message = message
        self.type = type
        
    def applyEffect(self, user, target):
        """ Apply the Leech to the target """
        leech = Leech(user, self.message)
        
        if not leech.immune(target.getTypes(), self.type):
            self.removePreviousLeech(target)
            
            target.secondaryEffects.append(leech)
            return [target.getHeader() + self.startMessage]
        
    def removePreviousLeech(self, pkmn):
        """ Checks if the pkmn already has a leech """
        effect = self.hasThisLeech(pkmn)
        if effect:
            pkmn.secondaryEffects.remove(effect)
                
    def hasThisLeech(self, pkmn):
        """ Returns if the pkmn receiving the leech already has a leech """
        for effect in pkmn.secondaryEffects:
            if effect.message is self.message:
                return effect
                
        return False 