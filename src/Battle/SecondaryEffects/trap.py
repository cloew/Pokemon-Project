from secondary_effect import SecondaryEffect

from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory

import random

class Trap(SecondaryEffect):
    """ Represents a Trap effect on a Pokemon """
    minTurns = 4
    ratio = 16
    
    def __init__(self, source, message, doneMessage):
        """ Builds a trap with the given message """
        self.source = source
        self.message = message
        self.doneMessage = doneMessage
        self.turns = self.getTurns()
        
        self.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.SOURCE)
        
    def getTurns(self):
        """ Returns the 4-5 turns """
        return Trap.minTurns + random.randint(0, 1)
        
    def afterTurn(self, owner):
        """ Does the damage of the Trap """
        messages = [owner.getHeader() + self.message]
        messages += self.damage(owner)
        
        if len(messages) is not 2:
            messages += self.decrementTurns(owner)
        
        return messages
        
    def damage(self, owner):
        """ Damages the user """
        return owner.takeDamage(self.getDamage(owner))
        
    def getDamage(self, owner):
        """ Returns the damage the Trap causes """
        return owner.getRatioOfHealth(Trap.ratio)
        
    def decrementTurns(self, owner):
        """ Decrement turns left for the Trap """
        messages = []
        self.turns = self.turns - 1
        
        if self.turns == 0:
            owner.secondaryEffects.remove(self)
            messages.append(owner.getHeader() + self.doneMessage)
        
        return messages