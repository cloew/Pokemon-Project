from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate
from Battle.SecondaryEffects.confusion import Confusion

class ConfuseDelegate(EffectDelegate):
    """ Represents an effect that confuses the opponent """
    
    def __init__(self, affectUser):
        """ Build the Confuse Delegate """
        self.affectUser = affectUser
        
    def applyEffect(self, user, target):
        """ Apply the Confusion to the target """
        pkmn = self.getEffectedPokemon(user, target)
        message = pkmn.getHeader()
        
        if not self.isConfused(pkmn):
            pkmn.secondaryEffects.append(Confusion())
            message = message + Confusion.start
        else:
            message = message + Confusion.already
            
        return [message]
                
    def isConfused(self, pkmn):
        """ Returns if the Pkmn is already confused """
        for effect in pkmn.secondaryEffects:
            if effect.__class__ == Confusion:
                return True
                
        return False 