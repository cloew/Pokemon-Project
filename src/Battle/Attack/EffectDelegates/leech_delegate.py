from Battle.SecondaryEffects.leech import Leech

class LeechDelegate :
    """ Represents an effect that slowly heals the user """
    
    def __init__(self, startMessage, message, type):
        """ Build the Leech Delegate """
        self.startMessage = startMessage
        self.message = message
        self.type = type
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the Leech to the target """
        leech = Leech(actingSide.currPokemon, self.message)
        
        if not leech.immune(otherSide.currPokemon.getTypes(), type):
            self.removePreviousLeech(otherSide)
            otherSide.secondaryEffects.append(leech)
            return [otherSide.getHeader() + self.startMessage]
        
    def removePreviousLeech(self, side):
        """ Checks if the side already has a leech """
        effect = self.hasThisLeech(side)
        if effect:
            side.secondaryEffects.remove(effect)
                
    def hasThisLeech(self, side):
        """ Returns if the side receiving the leech already has a leech """
        for effect in side.secondaryEffects:
            if effect.message is self.message:
                return effect
                
        return False 