from Battle.Status.status import Status

import random

class Freeze(Status):
    """ Represents a freeze status """
    abbr = "FRZ"
    start = " was frozen solid."
    intermittent = " is frozen solid."
    done = " thawed out."
    
    def __init__(self):
        self.setStatMods()
        
    def thawed(self, rand):
        """ Returns whether the Status is over """
        return rand == 0
        
    def getRandom(self):
        """ Returns a random # from 0-4 """
        return random.randint(0, 4)
        
    def immobilized(self, side):
        """ Returns whether the status prevents an action """
        messages = [side.getHeader() + Freeze.intermittent]
        
        if self.thawed(self.getRandom()):
            messages = messages + self.getDoneMessage(side)
            side.currPokemon.setStatus(Status())
        
        return True, messages