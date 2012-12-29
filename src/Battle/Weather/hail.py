from Battle.Weather.weather import Weather

class Hail(Weather):
    """ Represents Hail weather """
    type = "HAIL"
    
    def __init__(self):
        """ Build the Hail Weather """
        Weather.__init__(self, "It's hailing.")
    
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        messages = []
        if not self.immune(pokemon):
            messages += pokemon.takeRatioOfHealthAsDamage(16)
        messages += Weather.performWeatherEffectOnPokemon(pokemon)
        return messages
        
    def immune(self, pokemon):
        """ Returns if the pokemon is immune to Hail Damage """
        return "ICE" in pokemon.getTypes()