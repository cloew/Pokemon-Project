import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.Attack.EffectDelegates.diverge_on_first_turn_delegate import DivergeOnFirstTurnDelegate

class diverge(unittest.TestCase):
    """ Test cases of diverge """
    
    def  setUp(self):
        """ Build the Pkmn and Effects for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.divergeEffects = [BuildEffectDelegate(), BuildEffectDelegate()]
        self.normalEffects = [BuildEffectDelegate()]
        self.message = BuildEffectDelegate().message
        
        self.delegate = DivergeOnFirstTurnDelegate(self.divergeEffects, self.normalEffects)
        
    def firstTurn(self):
        """ Test that the diverge effects are called when the user has not used a move yet """
        self.user.lastAction = None
        diverge = self.delegate.diverge(self.user, self.target)
        assert diverge, "Should diverge"
        
    def notFirstTurn(self):
        """ Test that the regular effects are called when the user has used a move """
        self.user.lastAction = 1
        diverge = self.delegate.diverge(self.user, self.target)
        assert not diverge, "Should not diverge when the user has already done a move"

# Collect all test cases in this class on 
testcasesDiverge = ["firstTurn", "notFirstTurn"]
suiteDiverge = unittest.TestSuite(map(diverge, testcasesDiverge))

##########################################################

# Collect all test cases in this file
suites = [suiteDiverge]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()