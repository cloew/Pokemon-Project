

class Ability:
    """ Represents a Pokemon's ability """
    stabMod = 1.5
    
    def afterTurn(self, thisSide, otherSide):
        """ Perform after a turn  """
        return []
        
    def effectiveness(self, side):
        """ Return effectiveness mods """
        
        
    # Effects on Crit
    def giveCrit(self, critMod):
        """ Perform on a critical hit """
        return critMod
        
    def takeCrit(self, critMod, thisSide, otherSide):
        """ Perform on a critical hit """
        return critMod, []
        
        
        
        
    def onContact(self, side):
        """ Perform on attack that makes contact """
        
    def onDamage(self, side, damage):
        """ Perform on damage """
        
    def onEntry(self):
        """ Perform when a Pkmn arrives in the battle """
        
    def onFlinch(self, side):
        """ Perform on Flinch """
        
    def onLowHealth(self, side, status):
        """ Perform on low health """
        
    def onStab(self):
        """ Return the STAB mod """
        return self.stabMod
        
    def onStatMod(self, side, stat, degree, selfInflicted):
        """ Perform when a stat is modded """
        return degree, [] #  Returns a modified degree and any messages related to that
    
    def onStatus(self, side, status):
        """ Perform on application of status """
        return []
    
    def onSwitch(self):
        """ Perform on switch """
        
    
    def callEffects(self, thisSide, otherSide):
        """ Call the effects the ability has """
        messages = []
        print "In here"
        for effect in self.effects:
            effectMessages = effect.applyEffect(thisSide, otherSide)
            messages = messages + effectMessages
            
        return messages