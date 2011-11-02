from Battle.Attack.EffectDelegates.randomstatmod_delegate import RandomStatModDelegate
from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class pickRandStat(unittest.TestCase):
    """ Test that pickRandStat returns a random stat """
    
    def setUp(self):
        """ Builds the Delegate """
        self.delegate = RandomStatModDelegate(2, 1)
        
    def stat(self):
        """ Test that the get Header returns the correct header """
        stat = self.delegate.pickRandStat()
        assert stat in RandomStatModDelegate.stats, "Stat should be in random stats"
        
testcasesPickRandStat = ["stat"]
suitePickRandStat = unittest.TestSuite(map(pickRandStat, testcasesPickRandStat)) 

#########################################################
 
suites = [suitePickRandStat]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()