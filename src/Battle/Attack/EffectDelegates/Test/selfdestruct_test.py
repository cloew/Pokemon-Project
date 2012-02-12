import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.selfdestruct_delegate import SelfDestructDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.delegate = SelfDestructDelegate()
        
    def selfDestructed(self):
        """ Test that the user self destructs (aka dies) """
        self.delegate.applyEffect(self.user, None)
        assert self.user.getCurrHP() == 0, "Pkmn should have fainted"
    
    def message(self):
        """ Test that the user self destructs (aka dies) """
        messages = self.delegate.applyEffect(self.user, None)
        message = self.user.getHeader() + SelfDestructDelegate.message
        assert len(messages) == 1, "Should get 1 message"
        assert messages[0] == message, "Should get the Pkmn's header and the Delegate's message"

# Collect all test cases in this class
testcasesApplyEffect = ["selfDestructed", "message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()