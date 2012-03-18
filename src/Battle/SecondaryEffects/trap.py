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
        
    def afterTurn(self, pkmn):
        """ Does the damage of the Trap """
        messages = [pkmn.getHeader() + self.message]
        messages += self.damage(pkmn)
        
        if len(messages) is not 2:
            messages += self.decrementTurns(pkmn)
        
        return messages
        
    def damage(self, pkmn):
        """ Damages the user """
        return pkmn.takeDamage(self.getDamage(pkmn))
        
    def getDamage(self, pkmn):
        """ Returns the damage the Trap causes """
        return pkmn.getRatioOfHealth(Trap.ratio)
        
    def decrementTurns(self, pkmn):
        """ Decrement turns left for the Trap """
        messages = []
        self.turns = self.turns - 1
        
        if self.turns == 0:
            pkmn.secondaryEffects.remove(self)
            messages.append(pkmn.getHeader() + self.doneMessage)
        
        return messages