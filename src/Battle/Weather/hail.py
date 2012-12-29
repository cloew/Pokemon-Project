from Battle.Weather.weather import Weather

class Hail(Weather):
    """ Represents Hail weather """
    type = "HAIL"
    betweenRoundsMessage = "It's hailing."
    
    def __init__(self):
        """ Build the Hail Weather """
        Weather.__init__(self)
    
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        messages = []
        if not self.immune(pokemon):
            messages.append("{0} was buffeted by the hail.".format(pokemon.getName()))
            messages += pokemon.takeRatioOfHealthAsDamage(16)
        messages += Weather.performWeatherEffectOnPokemon(self, pokemon)
        return messages
        
    def immune(self, pokemon):
        """ Returns if the pokemon is immune to Hail Damage """
        return "ICE" in pokemon.getTypes()