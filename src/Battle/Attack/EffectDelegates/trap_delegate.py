from Battle.SecondaryEffects.trap import Trap

class TrapDelegate :
    """ Represents an effect that traps the opponent """
    
    def __init__(self, startMessage, message, doneMessage):
        """ Build the Trap Delegate """
        self.startMessage = startMessage
        self.message = message
        self.doneMessage = doneMessage
        
    def applyEffect(self, user, target):
        """ Apply the trap to the opponent """
        self.removePreviousTrap(target)
        target.secondaryEffects.append(Trap(self.message, self.doneMessage))
        return [target.getHeader() + self.startMessage]
        
    def removePreviousTrap(self, pkmn):
        """ Removes any previous implementations of the trap """
        effect = self.hasThisTrap(pkmn)
        if effect:
            pkmn.secondaryEffects.remove(effect)
                
    def hasThisTrap(self, pkmn):
        """ Returns if the pkmn has the same trap this delegate applies """
        for effect in pkmn.secondaryEffects:
            if effect.message == self.message:
                return effect
                
        return False 