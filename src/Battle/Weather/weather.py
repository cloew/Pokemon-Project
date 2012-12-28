
class Weather:
    """ Represents a Weather Effect in a Pokemon Battle """
    type = None
    
    def __init__(self, betweenTurnsMessage):
        """ Build the Weather effect """
        self.betweenTurnsMessage = betweenTurnsMessage
        
    def betweenTurns(self, playerSide, opponentSide):
        """ Function to handle events Between Turns """
        messages = []
        
        for pokemon in playerSide.pkmnInPlay + opponentSide.pkmnInPlay:
            messages += self.performWeatherEffectOnPokemon(pokemon)
        
        messages.append(self.betweenTurnsMessage)
        return messages
        
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        # Do damage in sub-classes
        # Should call Pokemon's ability
        return [] # Should return a list of messages