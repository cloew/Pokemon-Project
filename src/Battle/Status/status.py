
class Status:
    """ Represents a Status on a Pokemon """
    
    
    def __init__(self):
        """ Build a Status """
        self.abbr = "   "
        self.setStatMods()
                                
    def setStatMods(self):
        self.statMods = {"ATK":1, "DEF":1, "SPD":1, "SATK":1, "SDEF":1, 
                                "ACC":1, "EVAS":1, "CRT":1, "HP":1}
        
    def immobilized(self, side):
        """ Returns whether the status prevents an action """
        return False, []
        
    def afterTurn(self, side):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        return []
        
    def getStatMod(self, stat):
        """ Returns modifier from the status for the stat """
        return self.statMods[stat]
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types is immune to the status """
        
    def getDoneMessage(self, side):
        """  Returns the string to be displayed when the function ends """
        return [side.getHeader() + self.done]
        
    