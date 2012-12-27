import unittest
from Test.test_helper import *

from Battle.Weather.weather import Weather

class betweenTurns(unittest.TestCase):
    """ Test cases of betweenTurns """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.message = "Some Message"
        self.weather = Weather(self.message)
        
    def betweenTurnsMessage(self):
        """ Test that betweenTurns returns the Weather's between turns message """
        messages = self.weather.betweenTurns(None, None)
        assert messages == [self.message], "Should receive the weather's between turn message"

# Collect all test cases in this class
testcasesBetweenTurns = ["betweenTurnsMessage"]
suiteBetweenTurns = unittest.TestSuite(map(betweenTurns, testcasesBetweenTurns))

##########################################################

# Collect all test cases in this file
suites = [suiteBetweenTurns]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()