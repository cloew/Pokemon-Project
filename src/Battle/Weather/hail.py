from Battle.Weather.weather import Weather

class Hail(Weather):
    """ Represents Hail weather """
    type = "HAIL"
    startMessage = "It started to hail."
    betweenRoundsMessage = "It's hailing."
    overMessage = "The hailstorm subsided."
    
    def __init__(self, overCallbackFunction=None, turns=-1, forever=True):
        """ Build the Hail Weather """
        Weather.__init__(self, overCallbackFunction=overCallbackFunction, turns=turns, forever=forever)
    
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