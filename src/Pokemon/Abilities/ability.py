
class Ability:
    """ Represents a Pokemon's ability """
        
    def effectiveness(self, side):
        """ Return effectiveness mods """
        
    def onContact(self, side):
        """ Perform on attack that makes contact """
        
    def onDamage(self, side, damage):
        """ Perform on damage """
        
    def onFlinch(self, side):
        """ Perform on Flinch """
        
    def onLowHealth(self, side, status):
        """ Perform on low health """
        
    def onStatMod(self, side, stat, degree):
        """ Perform when a stat is modded """
        return degree, [] #  Returns a modified degree and any messages related to that
    
    def onStatus(self, side, status):
        """ Perform on application of status """
        return []
    
    def onSwitch(self): # Maybe onEntry
        """ Perform on switch """