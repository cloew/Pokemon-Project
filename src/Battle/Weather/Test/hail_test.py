import unittest
from Test.test_helper import *

from Battle.Weather.hail import Hail

class immune(unittest.TestCase):
    """ Test cases of immune """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.weather = Hail()
        self.pkmn = BuildPokemonBattleWrapper()
        
    def immune(self):
        """ Test that an Ice-type Pokemon is immune """
        self.pkmn.setTypes(["ICE"])
        assert self.weather.immune(self.pkmn), "Ice-type pokemon should be immune"
        
    def notImmune(self):
        """ Test that a non-Ice-type Pokemon is not immune """
        self.pkmn.setTypes(["GRASS"])
        assert not self.weather.immune(self.pkmn), "Non-Ice-type pokemon should not be immune"

# Collect all test cases in this class
testcasesImmune = ["immune", "notImmune"]
suiteImmune = unittest.TestSuite(map(immune, testcasesImmune))

##########################################################

# Collect all test cases in this file
suites = [suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()