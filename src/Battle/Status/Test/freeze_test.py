from Battle.Status.freeze import Freeze

from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class thawed(unittest.TestCase):
    """ Test that thawed returns the correct values """
    
    def setUp(self):
        """ Builds the Freeze status"""
        self.status = Freeze()
    
    def thawed(self):
        """ Test that thawed returns correctly when the staus should thaw """
        assert self.status.thawed(0), "Should thaw on zero"
        
    def notThawed(self):
        """ Test that thawed returns correctly when the staus should not thaw """
        for i in range(1, 5):
            assert not self.status.thawed(i), "Should not thaw on anything other than zero"

        
        
testcasesThawed = ["thawed", "notThawed"]
suiteThawed = unittest.TestSuite(map(thawed, testcasesThawed))

##########################################################
 
suites = [suiteThawed]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()