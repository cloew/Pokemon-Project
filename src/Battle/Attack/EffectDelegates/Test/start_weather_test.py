import unittest
from Test.test_helper import *

from Battle.Attack.EffectDelegates.start_weather_delegate import StartWeatherDelegate
from Battle.Weather.weather import Weather
from Battle.Weather.hail import Hail

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the environment and effect delegate for the test """
        self.environment = BattleEnvironment()
        self.effect = StartWeatherDelegate(Hail.type)
        
    def weatherChanges(self):
        """ Test that the weather changes when the effect is applied """
        assert self.environment.weather.type is None, "Should have No Weather at first"
        self.effect.applyEffect(None, None, self.environment)
        assert self.environment.weather.type == Hail.type, "Should have Hail Weather at first"
        
    def weatherMessage(self):
        """ Test that the weather changes when the effect is applied """
        messages = self.effect.applyEffect(None, None, self.environment)
        assert messages == [Hail.startMessage], "Should have the Hail Start Message"

# Collect all test cases in this class
testcasesApplyEffect = ["weatherChanges", "weatherMessage"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()