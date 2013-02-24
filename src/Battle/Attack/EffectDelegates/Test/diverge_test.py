import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.Attack.EffectDelegates.diverge_delegate import DivergeDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Effects for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.divergeEffects = [BuildEffectDelegate(), BuildEffectDelegate()]
        self.normalEffects = [BuildEffectDelegate()]
        self.message = BuildEffectDelegate().message
        
        self.delegate = DivergeDelegate(self.divergeEffects, self.normalEffects)
        
    def diverge(self):
        """ Test that the diverge effects are called when the effect should diverge """
        self.delegate.diverging = True
        messages = self.delegate.applyEffect(self.user, self.target, None)
        assert messages == [self.message, self.message], "Should get messages from all the Diverge Effects"
        
    def normal(self):
        """ Test that the regular effects are called when the effect should not diverge """
        self.delegate.diverging = False
        messages = self.delegate.applyEffect(self.user, self.target, None)
        assert messages == [self.message], "Should get messages from all the Normal Effects"

# Collect all test cases in this class on 
testcasesApplyEffect = ["diverge", "normal"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()