import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.flinch_delegate import FlinchDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.target = BuildPokemonBattleWrapper()
        self.delegate = FlinchDelegate()
        
    def flinch(self):
        """ Test that the target is set to flinch """
        messages = self.delegate.applyEffect(None, self.target, None)
        assert messages == [], "Should not receive any messages"
        assert self.target.flinching, "Target should be flinching"

# Collect all test cases in this class
testcasesApplyEffect = ["flinch"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()