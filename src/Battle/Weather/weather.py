
class Weather:
    """ Represents a Weather Effect in a Pokemon Battle """
    type = None
    
    def __init__(self, betweenRoundsMessage):
        """ Build the Weather effect """
        self.betweenRoundsMessage = betweenRoundsMessage
        
    def betweenRounds(self, playerSide, opponentSide):
        """ Function to handle events Between Rounds """
        messages = []
        if not self.betweenRoundsMessage is None:
            messages.append(self.betweenRoundsMessage)
        
        allPkmn = playerSide.pkmnInPlay + opponentSide.pkmnInPlay
        for pokemon in allPkmn:
            messages += self.performWeatherEffectOnPokemon(pokemon)
        return messages
        
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        # Do damage in sub-classes
        # Should call Pokemon's ability
        return [] # Should return a list of messages