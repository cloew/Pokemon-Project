import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.Attack.EffectDelegates.diverge_on_faint_delegate import DivergeOnFaintDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
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
        messages = self.delegate.applyEffect(self.user, self.target)
        assert messages == [self.message, self.message], "Should get messages from all the Diverge Effects"
        
    def notFainted(self):
        """ Test that the regular effects are called when the target is not fainted """
        messages = self.delegate.applyEffect(self.user, self.target)
        assert messages == [self.message], "Should get messages from all the Normal Effects"

# Collect all test cases in this class on 
testcasesApplyEffect = ["fainted", "notFainted"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()