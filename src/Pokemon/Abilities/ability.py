
class Ability:
    """ Represents a Pokemon's ability """
    
    def onContact(self, side):
        """ Perform on attack that makes contact """
        
    def effectiveness(self, side):
        """ Return effectiveness mods"""
        
    def onStatMod(self, side, stat):
        """ Perform when a stat is modded """
    
    def onLowHealth(self, side, status):
        """ Perform on low health """
    
    def onStatus(self, side, status):
        """ Perform on application of status """
        return []
    
    def onSwitch(self): # Maybe onEntry
        """ Perform on switch """