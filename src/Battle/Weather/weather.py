
class Weather:
    """ Represents a Weather Effect in a Pokemon Battle """
    
    def __init__(self, betweenTurnsMessage):
        """ Build the Weather effect """
        self.betweenTurnsMessage = betweenTurnsMessage
        
    def betweenTurns(self, playerSide, opponentSide):
        """ Function to handle events Between Turns """
        return [self.betweenTurnsMessage]