
class Weather:
    """ Represents a Weather Effect in a Pokemon Battle """
    type = None
    betweenRoundsMessage = None
    overMessage = None
    
    def __init__(self, turns=-1, forever=True):
        """ Build the Weather effect """
        self.turns = 5
        self.forever = forever
        
    def betweenRounds(self, playerSide, opponentSide):
        """ Function to handle events Between Rounds """
        messages = []
        if self.over():
            self.addOverMessage(messages)
        else:
            self.addRoundMessage(messages)
            self.affectEachPokemon(playerSide.pkmnInPlay + opponentSide.pkmnInPlay, messages)
        return messages
        
    def over(self):
        """ Retuns if the round is over """
        if round > 0:
            round -= 1
        return round == 0 and not self.forever
        
    def addRoundMessage(self, messages):
        """ Adds the Round Message to the messages list """
        if not self.betweenRoundsMessage is None:
            messages.append(self.betweenRoundsMessage)
            
    def addOverMessage(self, messages):
        """ Add the message for the Weather when it is over """
        if not self.overMessage is None:
            messages.append(self.overMessage)
    
    def affectEachPokemon(self, allPokemon, messages):
        """ Have the weather affect each Pokemon """
        for pokemon in allPokemon:
            messages += self.performWeatherEffectOnPokemon(pokemon)
        
    def performWeatherEffectOnPokemon(self, pokemon):
        """ Performs the weather's effect on the Pokemon """
        # Do damage in sub-classes
        # Should call Pokemon's ability
        return [] # Should return a list of messages