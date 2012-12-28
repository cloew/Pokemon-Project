import unittest
from Test.test_helper import *

from Battle.Weather.weather import Weather

class betweenTurns(unittest.TestCase):
    """ Test cases of betweenTurns """
    
    def  setUp(self):
        """ Build the BattleSides and weather for the test """
        self.message = "Some Message"
        self.weather = Weather(self.message)
        self.playerSide = BuildBattleSide()
        self.opponentSide = BuildBattleSide()
        
    def betweenTurnsMessage(self):
        """ Test that betweenTurns returns the Weather's between turns message """
        messages = self.weather.betweenTurns(self.playerSide, self.opponentSide)
        assert messages == [self.message], "Should receive the weather's between turn message"

# Collect all test cases in this class
testcasesBetweenTurns = ["betweenTurnsMessage"]
suiteBetweenTurns = unittest.TestSuite(map(betweenTurns, testcasesBetweenTurns))

##########################################################

class performWeatherEffectOnPokemon(unittest.TestCase):
    """ Test cases of performWeatherEffectOnPokemon """
    
    def  setUp(self):
        """ Build the Pokemon Battle Wrapper and weather for the test """
        self.message = "Some Message"
        self.weather = Weather(self.message)
        self.pkmn = BuildPokemonBattleWrapper()
        
    def performWeatherEffectOnPokemonMessage(self):
        """ Test that performWeatherEffectOnPokemon returns the Weather's between turns message """
        messages = self.weather.performWeatherEffectOnPokemon(self.pkmn)
        assert messages == [], "Should receive an empty between turn message for each Pokemon"

# Collect all test cases in this class
testcasesPerformWeatherEffectOnPokemon = ["performWeatherEffectOnPokemonMessage"]
suitePerformWeatherEffectOnPokemon = unittest.TestSuite(map(performWeatherEffectOnPokemon, testcasesPerformWeatherEffectOnPokemon))

##########################################################

# Collect all test cases in this file
suites = [suiteBetweenTurns, suitePerformWeatherEffectOnPokemon]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()