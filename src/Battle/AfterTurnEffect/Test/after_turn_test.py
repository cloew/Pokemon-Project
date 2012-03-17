import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.AfterTurnEffect.after_turn_effect import AfterTurnEffect

class attemptAfterTurn(unittest.TestCase):
    """ Test cases of attemptAfterTurn """
    
    def  setUp(self):
        """ Build the Pkmn and AfterTurnEffect for the test """
        self.effect = AfterTurnEffect()
        self.pkmn = BuildPokemonBattleWrapper()
        
    def fainted(self):
        """ Test that the Effect is not performed when the pkmn has fainted """
        self.pkmn.faint()
        messages = self.effect.attemptAfterTurn(self.pkmn)
        assert messages == [], "Should receive no messages since nothing was performed"
        
    def notFainted(self):
        """ Test that the Effect is performed when the pkmn has fainted """
        messages = self.effect.attemptAfterTurn(self.pkmn)
        assert messages == [AfterTurnEffect.message], "Should receive messages from afterTurn function"

# Collect all test cases in this class
testcasesAttemptAfterTurn = ["fainted", "notFainted"]
suiteAttemptAfterTurn = unittest.TestSuite(map(attemptAfterTurn, testcasesAttemptAfterTurn))

##########################################################

# Collect all test cases in this file
suites = [suiteAttemptAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()