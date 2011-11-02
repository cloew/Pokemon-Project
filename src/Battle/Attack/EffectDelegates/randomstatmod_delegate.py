from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate

import random

class RandomStatModDelegate(StatModDelegate):
    """ Handles modifying stats """
    
    stats = ["ATK", "DEF", "SPD", "SATK", "SDEF", "ACC", "EVAS"]
    
    def __init__(self, degree, side):
        """ Builds a StatModDelegate """
        self.degree = degree
        self.affectUser = side
    
    def applyEffect(self, actingSide, otherSide):
        """ Applies the Deleagates effect """
        self.stat = self.pickRandStat()
        
        return super(RandomStatModDelegate, self).applyEffect(actingSide, otherSide)
        
    def pickRandStat(self):
        """ Returns a random stat """
        i = random.randint(0, len(RandomStatModDelegate.stats)-1)
        return RandomStatModDelegate.stats[i]