import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.heal_ratio_delegate import HealByRatioDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = HealByRatioDelegate(2)
        
    def message(self):
        """ Test that the message is returned properly """
        messages = self.delegate.applyEffect(self.pkmn, None) 
        
        message = self.pkmn.getHeader() + HealByRatioDelegate.message
        assert len(messages) == 1, "Should receive one message"
        assert messages[0] == message, "Should be the Pokmn's header and the Delegates message"

# Collect all test cases in this class
testcasesApplyEffect = ["message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()