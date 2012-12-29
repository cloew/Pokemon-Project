from Battle.Weather.weather import Weather

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
        self.weather = Weather()