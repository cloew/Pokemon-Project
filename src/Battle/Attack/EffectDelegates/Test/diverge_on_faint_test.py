import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.Attack.EffectDelegates.diverge_on_faint_delegate import DivergeOnFaintDelegate

class diverge(unittest.TestCase):
    """ Test cases of diverge """
    
    def  setUp(self):
        """ Build the Pkmn and Effects for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.divergeEffects = [BuildEffectDelegate(), BuildEffectDelegate()]
        self.normalEffects = [BuildEffectDelegate()]
        self.message = BuildEffectDelegate().message
        
        self.delegate = DivergeOnFaintDelegate(self.divergeEffects, self.normalEffects)
        
    def fainted(self):
        """ Test that the diverge effects are called when the target has fainted """
        self.target.faint()
        diverge = self.delegate.diverge(self.user, self.target)
        assert diverge, "Should diverge"
        
    def notFainted(self):
        """ Test that the regular effects are called when the target is not fainted """
        diverge = self.delegate.diverge(self.user, self.target)
        assert not diverge, "Should not diverge when the target is not fainted"

# Collect all test cases in this class on 
testcasesDiverge = ["fainted", "notFainted"]
suiteDiverge = unittest.TestSuite(map(diverge, testcasesDiverge))

##########################################################

# Collect all test cases in this file
suites = [suiteDiverge]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()