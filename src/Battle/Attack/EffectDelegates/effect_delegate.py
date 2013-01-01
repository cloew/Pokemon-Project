

class EffectDelegate(object):
    """ Represents an Effect on an Attack """
    message = ""
    
    def getEffectedPokemon(self, user, target):
        """ Returns the pkmn that will be effected """
        if self.affectUser:
            return user
        else:
            return target
    
    def tryToApplyEffect(self, user, target, environment):
        """ Applies Effect as long as the Effect can handle the 
        Faint Status of the given User and Target """
        if self.faintHandler.cantHandle(user = user, target = target, effect = self):
            return []
            
        return self.applyEffect(user, target, environment)
        
    def applyEffect(self, user, target, environment):
        """ Applies effect -- Should be overridden by subclasses """
        return [EffectDelegate.message]
        
    def isCharging(self, user, environment):
        """ Performs any charging the attack needs this turn in battle
        Returns if the attack should not complete becauser of charging """
        return False
        
    def stopCharge(self, user):
        """ Stop Charging """
        
    def performEffects(self, effects, user, target, environment):
        """ Perform the effects given """
        messages = []
        for effect in effects:
            messages += effect.tryToApplyEffect(user, target, environment)
        return messages