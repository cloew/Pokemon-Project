import random

class CritDelegate:
    """ Handles how crits are applied """
    critMods =[.0655, .125, .25, 1/3.0, .5, .75, 1]
    
    def __init__(self, base):
        """ Builds a crit delegate, based on the core level """
        self.base  = base
        
    def crit(self, actingSide):
        """ Returns whether the attack crit or not """
        mod = self.base + actingSide.statMods["CRT"]
        ret = CritDelegate.critMods[mod] > random.random()
        return ret, "Critical hit!"
        