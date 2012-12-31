import unittest
from Test.test_helper import *

from Battle.battle_environment import BattleEnvironment
from Battle.Attack.EffectDelegates.weather_charge_delegate import WeatherChargeDelegate
from Battle.Weather.hail import Hail

class isCharging(unittest.TestCase):
    """ Test cases of isCharging """
    
    def  setUp(self):
        """ Build the Effect, Environment, and Pokemon for the test """
        self.turnToAttack = 1
        self.effect = WeatherChargeDelegate(2, self.turnToAttack, "Some Message", Hail.type)
        self.environment = BattleEnvironment()
        self.user = BuildPokemonBattleWrapper()
        
    def weatherCharged(self):
        """ Test that the weather can make the Attack be fully charged """
        self.environment.setWeather(self.effect.weatherType)
        assert not self.effect.isCharging(self.user, self.environment), "Effect should not be charging when the weather is right"
        
    def isCharging(self):
        """ Tests if isCharging returns correctly when it is charging """
        self.effect.turnOn = self.turnToAttack - 1
        assert self.effect.isCharging(self.user, self.environment), "Should be charging"
        
    def isNotCharging(self):
        """ Tests if isCharging returns correctly when it is not charging """
        self.effect.turnOn = self.turnToAttack
        assert not self.effect.isCharging(self.user, self.environment), "Should not be charging"
        

# Collect all test cases in this class
testcasesIsCharging = ["weatherCharged", "isCharging", "isNotCharging"]
suiteIsCharging = unittest.TestSuite(map(isCharging, testcasesIsCharging))

##########################################################

# Collect all test cases in this file
suites = [suiteIsCharging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()