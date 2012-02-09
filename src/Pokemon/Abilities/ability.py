

class Ability:
    """ Represents a Pokemon's ability """
    stabMod = 1.5
    
    def afterTurn(self, thisSide, otherSide):
        """ Perform after a turn  """
        return []
        
    def effectiveness(self, side):
        """ Return effectiveness mods """
        
    def canUseEffects(self):
        """ Return whether effects on damaging attacks can be used """
        return True
        
    # Effects on Crit
    def giveCrit(self, critMod):
        """ Perform on a critical hit """
        return critMod
        
    def takeCrit(self, critMod, thisSide, otherSide):
        """ Perform on a critical hit """
        return critMod, []
        
        
    def onAccuracy(self, accuracy):
        """ Perform on accuracy """
        return accuracy
        
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
        
    
    def callEffects(self, user, target):
        """ Call the effects the ability has """
        messages = []
        for effect in self.effects:
            effectMessages = effect.applyEffect(user, target)
            messages = messages + effectMessages
            
        return messages