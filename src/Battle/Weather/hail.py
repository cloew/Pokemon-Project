from Battle.Weather.weather import Weather

class Hail(Weather):
    """ Represents Hail weather """
    type = "HAIL"
    
    def __init__(self):
        """ Build the Hail Weather """
        Weather.__init__(self, "It's hailing.")
    
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        # Do damage in sub-classes
        return Weather.performWeatherEffectOnPokemon(pokemon)
        
    def immune(self, pokemon):
        """ Returns if the pokemon is immune to Hail Damage """
        return "ICE" in pokemon.getTypes()