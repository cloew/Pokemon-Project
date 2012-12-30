from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class StartWeatherDelegate(EffectDelegate):
    """ Represents an effect that starts a new type of weather """
    
    def __init__(self, weatherType):
        """ Build the Start Weather Delegate with the type of weather it starts """
        self.weatherType = weatherType
        
    def applyEffect(self, user, target, environment):
        """ Applies the delegates effect """
        return environment.setWeather(weatherType)