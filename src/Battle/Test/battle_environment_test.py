import unittest
from Test.test_helper import *

from Battle.battle_environment import BattleEnvironment

class clearWeather(unittest.TestCase):
    """ Test cases of clearWeather """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.environment = BattleEnvironment()
        self.environment.weather = None
        
    def weatherCleared(self):
        """ Test that clearWeather sets the Environment's weather to the base Weather class """
        assert self.environment.weather is None, "Environment should have no weather"
        self.environment.clearWeather()
        assert self.environment.weather.type is None, "Environment should have weather with No Type"
        
# Collect all test cases in this class
testcasesClearWeather = ["weatherCleared"]
suiteClearWeather = unittest.TestSuite(map(clearWeather, testcasesClearWeather))

##########################################################

# Collect all test cases in this file
suites = [suiteClearWeather]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()