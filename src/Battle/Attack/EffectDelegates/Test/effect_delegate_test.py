import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildFaintHandler

from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class getEffectedPokemon(unittest.TestCase):
    """ Test cases of getEffectedPokemon """
    
    def  setUp(self):
        """ Build the Pkmn and Effect for the test """
        self.delegate = EffectDelegate()
        
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
    def user(self):
        """ Test that if affectUser is True, the Pkmn returned is the user """
        self.delegate.affectUser = True
        pkmn = self.delegate.getEffectedPokemon(self.user, self.target)
        assert pkmn is  self.user, "Pkmn should be the user"
        
    def target(self):
        """ Test that if the target is fainted the effect does nothing """
        self.delegate.affectUser = False
        pkmn = self.delegate.getEffectedPokemon(self.user, self.target)
        assert pkmn is  self.target, "Pkmn should be the target"

# Collect all test cases in this class
testcasesGetEffectedPokemon = ["user", "target"]
suiteGetEffectedPokemon = unittest.TestSuite(map(getEffectedPokemon, testcasesGetEffectedPokemon))

##########################################################

class tryToApplyEffect(unittest.TestCase):
    """ Test cases of tryToApplyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Effect for the test """
        self.delegate = EffectDelegate()
        self.delegate.faintHandler = BuildFaintHandler("EITHER")
        
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
suites = [suiteGetEffectedPokemon, suiteTryToApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()