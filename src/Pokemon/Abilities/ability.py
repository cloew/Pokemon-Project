from Battle.AfterTurnEffect.after_turn_effect import AfterTurnEffect

class Ability(AfterTurnEffect):
    """ Represents a Pokemon's ability """
    stabMod = 1.5
    
    def afterTurn(self, pkmn):
        """ Perform after a turn  """
        return []
        
    def effectiveness(self, pkmn):
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
        
    def onContact(self, pkmn):
        """ Perform on attack that makes contact """
        
    def onDamage(self, pkmn, damage):
        """ Perform on damage """
        
    def onEntry(self):
        """ Perform when a Pkmn arrives in the battle """
        
    def onFlinch(self, pkmn):
        """ Perform on Flinch """
        
    def onLowHealth(self, pkmn, status):
        """ Perform on low health """
        
    def onStab(self):
        """ Return the STAB mod """
        return self.stabMod
        
    def onStatMod(self, pkmn, stat, degree, selfInflicted):
        """ Perform when a stat is modded """
        return degree, [] #  Returns a modified degree and any messages related to that
    
    def onStatus(self, pkmn, status):
        """ Perform on application of status """
        return []
    
    def onSwitch(self):
        """ Perform on switch """
        
    
    def callEffects(self, user):
        """ Call the effects the ability has """
        messages = []
        for effect in self.effects:
            effectMessages = effect.tryToApplyEffect(user, None)
            messages = messages + effectMessages
            
        return messages