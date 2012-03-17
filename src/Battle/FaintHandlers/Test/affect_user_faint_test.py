import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildEffectDelegate

from Battle.FaintHandlers.affect_user_faint import AffectUserFaintDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = AffectUserFaintDelegate()
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.effect = BuildEffectDelegate()
        
    def userFainted(self):
        """ Test that it can't handle the user fainting """
        self.user.faint()
        self.effect.affectUser = 1
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert cantHandle, "Shouldn't handle when the user is fainted"
        
    def userNotFainted(self):
        """ Test that it can handle when the user is not fainted """
        self.effect.affectUser = 1
        cantHandle = self.handler.cantHandle(user = self.user, effect = self.effect)
        assert not cantHandle, "Should handle when the user is not fainted"
        
    def targetFainted(self):
        """ Test that it can't handle the target fainting """
        self.target.faint()
        self.effect.affectUser = 0
        cantHandle = self.handler.cantHandle(target = self.target, effect = self.effect)
        assert cantHandle, "Shouldn't handle when the target is fainted"
        
    def targetNotFainted(self):
        """ Test that it can handle when the target is not fainted """
        self.effect.affectUser = 0
        cantHandle = self.handler.cantHandle(target = self.target, effect = self.effect)
        assert not cantHandle, "Should handle when the target is not fainted"

# Collect all test cases in this class
testcasesCantHandle = ["userFainted", "userNotFainted", "targetFainted", "targetNotFainted"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()