import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.FaintHandlers.either_faint import EitherFaintDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = EitherFaintDelegate()
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
    def user(self):
        """ Test that it can handle the user fainting """
        self.user.faint()
        cantHandle = self.handler.cantHandle(user = self.user, target = self.target)
        assert cantHandle, "Shouldn't handle when the user faints"
        
    def target(self):
        """ Test that it can't handle the target fainting """
        self.target.faint()
        cantHandle = self.handler.cantHandle(user = self.user, target = self.target)
        assert cantHandle, "Shouldn't handle when the target faints"
        
    def both(self):
        """ Test that it can't handle both pkmn fainting """
        self.user.faint()
        self.target.faint()
        cantHandle = self.handler.cantHandle(user = self.user, target = self.target)
        assert cantHandle, "Shouldn't handle when both pkmn faints"
        
    def neither(self):
        """ Test that it can handle neither pkmn fainting """
        cantHandle = self.handler.cantHandle(user = self.user, target = self.target)
        assert not cantHandle, "Should handle when neither faints"
        

# Collect all test cases in this class
testcasesCantHandle = ["user", "target", "both", "neither"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()