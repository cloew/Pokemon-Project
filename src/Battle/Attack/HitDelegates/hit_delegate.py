import random

class HitDelegate(object):
    """ Represents an Attack's ability to hit an opponent """
    accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 9,
                    1/3.0, 3/8.0, .428, 1/2.0, 3/5.0, 3/4.0]
                    
    message = "Attack missed."
  
    def __init__(self, parent, toHit):
        """ Build a core hit Delegate """
        self.parent = parent
        self.chanceToHit = toHit
    
    
    def hit(self, user, target):
        """ Returns whether or not an attack hit its target """
        return not self.dodging(target) and self.core(user, target), [self.message]
        
        
    def core(self, user, target):
        """ Calculates a random #, compares to chanceToHit to determine if it
        lands or not """
        accuracy = user.currPokemon.ability.onAccuracy(self.chanceToHit)
        accMod = HitDelegate.accMods[user.statMods["ACC"]]
        evasMod = HitDelegate.accMods[-1*target.statMods["EVAS"]]
        toHit = accuracy*accMod*evasMod
        return random.randint(0, 99) < toHit
        
    def dodging(self, target):
            """ Returns if the opp is dodging """
            return target.dodge is not None 