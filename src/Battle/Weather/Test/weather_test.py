import unittest
from Test.test_helper import *

from Battle.Weather.weather import Weather

class betweenRounds(unittest.TestCase):
    """ Test cases of betweenRounds """
    
    def  setUp(self):
        """ Build the BattleSides and weather for the test """
        self.message = "Some Message"
        self.weather = Weather()
        self.weather.betweenRoundsMessage = self.message
        self.playerSide = BuildBattleSide()
        self.opponentSide = BuildBattleSide()
        
    def betweenRoundsMessage(self):
        """ Test that betweenRounds returns the Weather's between turns message """
        messages = self.weather.betweenRounds(self.playerSide, self.opponentSide)
        assert messages == [self.message], "Should receive the weather's betweenRounds message"

# Collect all test cases in this class
testcasesBetweenRounds = ["betweenRoundsMessage"]
suiteBetweenRounds = unittest.TestSuite(map(betweenRounds, testcasesBetweenRounds))

##########################################################

class addRoundMessage(unittest.TestCase):
    """ Test cases of addRoundMessage """
    
    def  setUp(self):
        """ no setup for the test """
        
    def withMessage(self):
        """ Test that addRoundMessage adds the Weather's between rounds message """
        messages = []
        message = "Some Message"
        weather = Weather()
        weather.betweenRoundsMessage = message
        weather.addRoundMessage(messages)
        assert messages == [message], "Should receive the weather's betweenRoundsMessage"
        
    def noMessage(self):
        """ Test that addRoundMessage does not add a message when the Weather has no between rounds message """
        messages = []
        weather = Weather()
        weather.addRoundMessage(messages)
        assert messages == [], "Should receive no message when the Weather object has no message"

# Collect all test cases in this class
testcasesAddRoundMessage = ["withMessage", "noMessage"]
suiteAddRoundMessage = unittest.TestSuite(map(addRoundMessage, testcasesAddRoundMessage))

##########################################################

class performWeatherEffectOnPokemon(unittest.TestCase):
    """ Test cases of performWeatherEffectOnPokemon """
    
    def  setUp(self):
        """ Build the Pokemon Battle Wrapper and weather for the test """
        self.weather = Weather()
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
suites = [suiteBetweenRounds, suiteAddRoundMessage, suitePerformWeatherEffectOnPokemon]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()