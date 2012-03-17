

class EffectDelegate:
    """ Represents an Effect on an Attack """
    message = ""
    
    def tryToApplyEffect(self, user, target):
        """ Applies Effect as long as the Effect can handle the 
             Faint Status of the given user and Target """
        if user.fainted() or target.fainted():
            return []
            
        return self.applyEffect(user, target)
        
    def applyEffect(self, user, target):
        """ Applies effect -- Should be overridden by subclasses """
        return [EffectDelegate.message]