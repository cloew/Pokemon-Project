
class BattleMessage:
    """ Represents a message created during a battle """
    
    def __init__(self, message):
        """ Builds a BattleMessage with the given message """
        self.message = message
        self.fullyDisplayed = False
        
    def getMessageSlice(self, endIndex):
        """  Returns a slice of the message up to the last index provided """
        self.fullyDisplayed = (endIndex == self.length())
        return self.message[:endIndex]
        
    def length(self):
        """ Returns the length of the message """
        return len(self.message)