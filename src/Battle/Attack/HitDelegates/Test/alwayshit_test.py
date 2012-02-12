import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.HitDelegates.alwayshit_delegate import AlwaysHitDelegate

class checkHit(unittest.TestCase):
    """ Test cases of hit """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.delegate = AlwaysHitDelegate()
        
    def hit(self):
        """ Test that it always hits """
        hit = self.delegate.checkHit(100, 0)
        assert hit, "Should always hit"

# Collect all test cases in this class
testcasesCheckHit = ["hit"]
suiteCheckHit = unittest.TestSuite(map(checkHit, testcasesCheckHit))

##########################################################

# Collect all test cases in this file
suites = [suiteCheckHit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()