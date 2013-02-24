from weather import Weather
from hail import Hail

class WeatherFactory:
    """ Factory to create Weather Objects """
    weatherTypeDictionary = {Weather.type:Weather,
                             Hail.type:Hail}
    
    @staticmethod
    def buildWeatherFromType(type, environment, turns=-1, forever=True):
        """ Build a Weather object from a type """
        weatherClass = WeatherFactory.weatherTypeDictionary[type]
        return weatherClass(overCallbackFunction=environment.clearWeather, turns=turns, forever=forever)