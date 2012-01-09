from Battle.Status.status import Status

import random

class Sleep(Status):
    """ Represents a sleep status """
    abbr = "SLP"
    start = " fell asleep."
    intermittent = " is fast asleep."
    done = " woke up."
    
    min = 1
    max = 7
    
    def __init__(self):
        self.setStatMods()
        self.turns = self.getTurns()
        
    def getTurns(self):
        """ Returns a # of turns from 1-7 """
        return random.randint(Sleep.min, Sleep.max)
        
    def immobilized(self, pkmn):
        """ Returns whether the status prevents an action """
        messages = [pkmn.getHeader() + Sleep.intermittent]
        
        if self.turns == 0:
            messages= messages + self.getDoneMessage(pkmn)
            pkmn.currPokemon.setStatus(Status())
            return False, messages
        
        self.turns = self.turns - 1
        
        return True, messages