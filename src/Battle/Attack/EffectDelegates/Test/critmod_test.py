import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.critmod_delegate import CritModDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.degree = 2
        self.delegate = CritModDelegate(self.degree)
        
    def message(self):
        """ Test that the message returned is the CritMode Message """
        messages = self.delegate.applyEffect(self.user, self.target, None)
        
        assert len(messages) == 1, "Should have one message"
        assert messages[0] == CritModDelegate.message, "Should be the CritMod message"

# Collect all test cases in this class
testcasesApplyEffect = ["message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()