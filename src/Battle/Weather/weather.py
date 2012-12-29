
class Weather:
    """ Represents a Weather Effect in a Pokemon Battle """
    type = None
    
    def __init__(self, betweenRoundsMessage):
        """ Build the Weather effect """
        self.betweenRoundsMessage = betweenRoundsMessage
        
    def betweenRounds(self, playerSide, opponentSide):
        """ Function to handle events Between Rounds """
        messages = []
        self.addRoundMessage(messages)
        self.affectEachPokemon(playerSide.pkmnInPlay + opponentSide.pkmnInPlay, messages)
        return messages
        
    def addRoundMessage(self, messages):
        """ Adds the Round Message to the messages list """
        if not self.betweenRoundsMessage is None:
            messages.append(self.betweenRoundsMessage)
    
    def affectEachPokemon(self, allPokemon, messages):
        """ Have the weather affect each Pokemon """
        for pokemon in allPokemon:
            messages += self.performWeatherEffectOnPokemon(pokemon)
        
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        # Do damage in sub-classes
        # Should call Pokemon's ability
        return [] # Should return a list of messages