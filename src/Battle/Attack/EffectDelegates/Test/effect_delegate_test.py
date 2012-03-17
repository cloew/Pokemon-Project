import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class tryToApplyEffect(unittest.TestCase):
    """ Test cases of tryToApplyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Effect for the test """
        self.delegate = EffectDelegate()
        
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
    def userFainted(self):
        """ Test that if the user is fainted the effect does nothing """
        self.user.faint()
        messages = self.delegate.tryToApplyEffect(self.user, self.target)
        assert messages == [], "Effect should do nothing if the user has fainted"
        
    def targetFainted(self):
        """ Test that if the target is fainted the effect does nothing """
        self.target.faint()
        messages = self.delegate.tryToApplyEffect(self.user, self.target)
        assert messages == [], "Effect should do nothing if the target has fainted"
        
    def applyEffectCalled(self):
        """ Test that applyEffect is called otherwise """
        messages = self.delegate.tryToApplyEffect(self.user, self.target)
        assert messages == [EffectDelegate.message], "Effect should call applyEffect"

# Collect all test cases in this class
testcasesTryToApplyEffect = ["userFainted", "targetFainted", "applyEffectCalled"]
suiteTryToApplyEffect = unittest.TestSuite(map(tryToApplyEffect, testcasesTryToApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteTryToApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()