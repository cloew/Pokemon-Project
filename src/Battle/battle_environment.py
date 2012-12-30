from Battle.Weather.weather import Weather
from Battle.Weather.weather_factory import WeatherFactory

class BattleEnvironment:
    """ Represents the Environemnt a Battle is taking place in """
    
    def __init__(self):
        """ Build the Battle Environment default """
        # Eventually, this will need to receive the tile-type
        self.clearWeather()
        
    def betweenRounds(self, playerSide, opponentSide):
        """ Function to handle events Between Rounds """
        return self.weather.betweenRounds(playerSide, opponentSide)
        
    def clearWeather(self):
        """ Clears the weather """
        self.setWeather(Weather.type)
        
    def setWeather(self, type):
        """ Set teh weather to a weather of the given tyoe """
        self.weather = WeatherFactory.buildWeatherFromType(type, self)
        messages = self.weather.getStartMessage()
        return messages