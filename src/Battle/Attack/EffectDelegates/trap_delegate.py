from Battle.Attack.Trap.trap import Trap

class TrapDelegate :
    """ Represents an effect that traps the opponent """
    
    def __init__(self, startMessage, message):
        """ Build the Trap Delegate """
        self.startMessage = startMessage
        self.message = message
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the trap to the opponent """
        otherSide.afterEffects.append(Trap(self.message))
        return [otherSide.currPokemon.name + self.startMessage]