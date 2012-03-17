import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.FaintHandlers.target_faint import TargetFaintDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintDelegate for the test """
        self.handler = TargetFaintDelegate()
        self.target = BuildPokemonBattleWrapper()
        
    def targetFainted(self):
        """ Test that it can't handle the target fainting """
        self.target.faint()
        cantHandle = self.handler.cantHandle(target = self.target)
        assert cantHandle, "Shouldn't handle when the target is fainted"
        
    def targetNotFainted(self):
        """ Test that it can handle when the target is not fainted """
        cantHandle = self.handler.cantHandle(target = self.target)
        assert not cantHandle, "Should handle when the target is not fainted"

# Collect all test cases in this class
testcasesCantHandle = ["targetFainted", "targetNotFainted"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()