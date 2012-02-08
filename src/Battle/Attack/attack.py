from preconditions import PreconditionChecker
from resources.tags import Tags

class Attack:
    """ Represents an Attack """
    
    def __init__(self):
        self.hitDelegate = None
        self.damageDelegate = None
        self.speedDelegate = None
        
        self.effectDelegates = []
        
    def use(self, user, target):
        """ Uses the current attack Object in a Battle """
        messages = []
        
        # Check for pre attack factors
        preconditionChecker = PreconditionChecker(user, target, self)
        stop, preMessages = preconditionChecker.checkPreConditions()
        messages = preMessages
        if stop:
            return preMessages
            
        # Lower PP
        
        messages = messages + ["{0} USED {1}".format(user.getHeader(), self.name)]
        
        # Check for hit
        hit, hitMessages = self.hitDelegate.hit(user, target)
        if not hit:
            messages = messages + hitMessages
            messages = messages + self.applyEffectsOnMiss(user, target)
            return messages
          
        # Do damage
        message = self.damageDelegate.doDamage(user, target)
        if message and len(message) is not 0:
            messages = messages + message  

        # Check if effects should be used
        if self.preventEffects(user, target):
            return messages
        
        # Apply effects
        for effect in self.effectDelegates:
            effectMessages = effect.applyEffect(user, target)
            messages = messages + effectMessages
        
        return messages
        
    def addDelegate(self, delegateCategory, delegate):
        """ Adds a delegate to an Attack Object """
        if delegateCategory == Tags.effectDelegateTag:
            self.effectDelegates.append(delegate)
            return
        setattr(self, delegateCategory, delegate)
        
    def preventEffects(self, user, target):
        """ Return whether the effects are prevented """
        nullDamage = hasattr(self.damageDelegate, "isNull")
        canUse = user.getAbility().canUseEffects() and target.getAbility().canUseEffects()
        return not nullDamage and not canUse
        
    def applyEffectsOnMiss(self, user, target):
        """ Apply effects on miss """
        messages = []
        for effect in self.effectDelegates:
            if hasattr(effect, "applyOnMiss"):
                effectMessages = effect.applyEffect(user, target)
                messages = messages + effectMessages
            if hasattr(effect, "effectOnMiss"):
                effectMessages = effect.effectOnMiss(user, target)
                messages = messages + effectMessages
        return messages
        