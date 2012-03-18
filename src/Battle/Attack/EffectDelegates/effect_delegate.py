

class EffectDelegate(object):
    """ Represents an Effect on an Attack """
    message = ""
    
    def getEffectedPokemon(self, user, target):
        """ Returns the pkmn that will be effected """
        if self.affectUser:
            return user
        else:
            return target
    
    def tryToApplyEffect(self, user, target):
        """ Applies Effect as long as the Effect can handle the 
        Faint Status of the given User and Target """
        if self.faintHandler.cantHandle(user = user, target = target, effect = self):
            return []
            
        return self.applyEffect(user, target)
        
    def applyEffect(self, user, target):
        """ Applies effect -- Should be overridden by subclasses """
        return [EffectDelegate.message]
        
    def stopCharge(self, user):
        """ Stop Charging """