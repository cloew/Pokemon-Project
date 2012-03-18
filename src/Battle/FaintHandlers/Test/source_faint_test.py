import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.FaintHandlers.source_faint import SourceFaintDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = SourceFaintDelegate()
        self.source = BuildPokemonBattleWrapper()
        self.user = BuildPokemonBattleWrapper()
        self.effect = BuildEffectDelegate()
        
        self.effect.source = self.source
        self.user.secondaryEffects.append(self.effect)
        
    def userFainted(self):
        """ Test that it can't handle the user fainting """
        self.user.faint()
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert cantHandle, "Shouldn't handle when the user is fainted"
        assert self.effect in self.user.secondaryEffects, "The effect shouldnot be removed from the user"
        
    def userNotFainted(self):
        """ Test that it can handle when the user is not fainted """
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert not cantHandle, "Should handle when the user is not fainted"
        assert self.effect in self.user.secondaryEffects, "The effect should not be removed from the user"
        
    def sourceFainted(self):
        """ Test that it can't handle the source fainting """
        self.source.faint()
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert cantHandle, "Shouldn't handle when the source is fainted"
        assert not self.effect in self.user.secondaryEffects, "The effect should be removed from the user"
        
    def sourceNotFainted(self):
        """ Test that it can handle when the user is not fainted """
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert not cantHandle, "Should handle when the source is not fainted"
        assert self.effect in self.user.secondaryEffects, "The effect should not be removed from the user"

# Collect all test cases in this class
testcasesCantHandle = ["userFainted", "userNotFainted", "sourceFainted", "sourceNotFainted"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

class removeEffect(unittest.TestCase):
    """ Test cases of removeEffect """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = SourceFaintDelegate()
        self.source = BuildPokemonBattleWrapper()
        self.user = BuildPokemonBattleWrapper()
        self.effect = BuildEffectDelegate()
        
        self.effect.source = self.source
        self.user.secondaryEffects.append(self.effect)
        
    def removed(self):
        """ Test that it can't handle the user fainting """
        self.handler.removeEffect(self.user, self.effect)
        assert not self.effect in self.user.secondaryEffects, "The effect should be removed from the user"

# Collect all test cases in this class
testcasesRemoveEffect = ["removed"]
suiteRemoveEffect = unittest.TestSuite(map(removeEffect, testcasesRemoveEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle, suiteRemoveEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()