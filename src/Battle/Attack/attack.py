from preconditions import PreconditionsChecker
from resources.tags import Tags

class Attack:
    """ Represents an Attack """
    
    def __init__(self):
        self.hitDelegate = None
        self.damageDelegate = None
        self.speedDelegate = None
        
        self.effectDelegates = []
        
    #def use(self, actingSide, otherSide):
    def use(self, user, target):
        """ Uses the current attack Object in a Battle """
        #user = actingSide.currPokemon
        #target = otherSide.currPokemon
        messages = []
        
        # Check for pre attack factors
        preconditionChecker = PreconditionsChecker(user, target, self)
        stop, preMessages = preconditionChecker.checkPreConditions(user, target)
        messages = preMessages
        if stop:
            return preMessages
            
        # Lower PP
        
        messages = messages + ["{0} USED {1}".format(user.getHeader(), self.name)]
        
        # Check for hit
        hit, hitMessages = self.hitDelegate.hit(user, target)
        if not hit:
            messages = messages + hitMessages
            messages = messages + self.applyEffectsOnMiss(actingSide, otherSide)
            return messages
          
        # Do damage
        message = self.damageDelegate.doDamage(actingSide, otherSide)
        if message and len(message) is not 0:
            messages = messages + message  

        # Check if effects should be used
        if self.preventEffects(user, target):
            return messages
        
        # Apply effects
        for effect in self.effectDelegates:
            effectMessages = effect.applyEffect(actingSide, otherSide)
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
        canUse = user.ability.canUseEffects() and target.ability.canUseEffects()
        return not nullDamage and not canUse
        
    def applyEffectsOnMiss(self, actingSide, otherSide):
        """ Apply effects on miss """
        messages = []
        for effect in self.effectDelegates:
            if hasattr(effect, "applyOnMiss"):
                effectMessages = effect.applyEffect(actingSide, otherSide)
                messages = messages + effectMessages
            if hasattr(effect, "effectOnMiss"):
                effectMessages = effect.effectOnMiss(actingSide, otherSide)
                messages = messages + effectMessages
        return messages