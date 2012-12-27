from Battle.AfterTurnEffect.after_turn_effect import AfterTurnEffect
from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory

class Ability(AfterTurnEffect):
    """ Represents a Pokemon's ability """
    stabMod = 1.5
    
    def __init__(self):
        self.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
        
    def stopAttack(self, pkmn):
        """ Determines if the Pkmn should fail to Attack because of an Ability """
        return False, []
    
    def afterTurn(self, pkmn):
        """ Perform after a turn  """
        return []
        
    def effectiveness(self, pkmn):
        """ Return effectiveness mods """
        
    def canBeConfused(self, pkmn, messages):
        """ Return if the pokemon can be confused """
        return True
        
    def canUseEffects(self):
        """ Return whether effects on damaging attacks can be used """
        return True
        
    # Effects on Crit
    def giveCrit(self, critMod):
        """ Perform on a critical hit """
        return critMod
        
    def takeCrit(self, critMod, receiver, attacker):
        """ Perform on a critical hit """
        return critMod, []
        
        
    def onAccuracy(self, accuracy):
        """ Perform on accuracy """
        return accuracy
        
    def onContact(self, pkmn, attacker):
        """ Perform on attack that makes contact """
        return []
        
    def onCharge(self):
        """ Perform on Charge """
        
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
        
    
    def callEffects(self, user=None, target=None):
        """ Call the effects the ability has """
        messages = []
        for effect in self.effects:
            effectMessages = effect.tryToApplyEffect(user, target)
            messages = messages + effectMessages
            
        return messages