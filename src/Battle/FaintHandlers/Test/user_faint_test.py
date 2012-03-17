import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.FaintHandlers.user_faint import UserFaintDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = UserFaintDelegate()
        self.user = BuildPokemonBattleWrapper()
        
    def userFainted(self):
        """ Test that it can't handle the user fainting """
        self.user.faint()
        cantHandle = self.handler.cantHandle(user = self.user)
        assert cantHandle, "Shouldn't handle when the user is fainted"
        
    def userNotFainted(self):
        """ Test that it can handle when the user is not fainted """
        cantHandle = self.handler.cantHandle(user = self.user)
        assert not cantHandle, "Should handle when the user is not fainted"

# Collect all test cases in this class
testcasesCantHandle = ["userFainted", "userNotFainted"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()