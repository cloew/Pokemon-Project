import random

class CritDelegate:
    """ Handles how crits are applied """
    critMods = [.0655, .125, .25, 1/3.0, .5, .75, 1]
    critMessage = "Critical hit!"
    
    def __init__(self, base):
        """ Builds a crit delegate, based on the core level """
        self.base  = base
        
    def crit(self, user):
        """ Returns whether the attack crit or not """
        critChance = self.getCritChance(user)
        return self.checkForCrit(critChance, random.random())
        
    def getCritChance(self, user):
        """ Return the Crit Chance of the Attack """
        mod = self.base + user.statMods["CRT"]
        return CritDelegate.critMods[mod]
        
    def checkForCrit(self, critChance, rand):
        """ Return if the attack crits """
        ret =  critChance > rand
        return ret, CritDelegate.critMessage