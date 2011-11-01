from Battle.AfterTurnEffects.trap import Trap

class TrapDelegate :
    """ Represents an effect that traps the opponent """
    
    def __init__(self, startMessage, message, doneMessage):
        """ Build the Trap Delegate """
        self.startMessage = startMessage
        self.message = message
        self.doneMessage = doneMessage
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the trap to the opponent """
        self.removePreviousTrap(otherSide)
        otherSide.afterEffects.append(Trap(self.message, self.doneMessage))
        return [otherSide.getHeader() + self.startMessage]
        
    def removePreviousTrap(self, side):
        """ Removes any previous implementations of the trap """
        effect = self.hasThisTrap(side)
        if effect:
            side.afterEffects.remove(effect)
                
    def hasThisTrap(self, side):
        """ Returns if the side has the same trap this delegate applies """
        for effect in side.afterEffects:
            if effect.message == self.message:
                return effect
                
        return False 