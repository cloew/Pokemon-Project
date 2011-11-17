from resources.tags import Tags

class Attack:
    """ Represents an Attack """
    
    def __init__(self):
        self.hitDelegate = None
        self.damageDelegate = None
        self.speedDelegate = None
        
        self.effectDelegates = []
        
        self.conditionsToCheck = [self.checkLock, self.checkFlinch, self.checkCharging,
                                              self.checkEncore, self.checkStatus]
        
    def use(self, actingSide, otherSide):
        """ Uses the current attack Object in a Battle """
        user = actingSide.currPokemon
        target = otherSide.currPokemon
        messages = []
        
        # Check for pre attack factors
        stop, preMessages = self.checkPreConditions(actingSide, otherSide)
        messages = preMessages
        if stop:
            return preMessages
        
        messages = messages + ["{0} USED {1}".format(actingSide.getHeader(), self.name)]
        
        # Check for hit
        hit, hitMessages = self.hitDelegate.hit(actingSide, otherSide)
        if not hit:
            messages = messages + hitMessages
            messages = messages + self.applyEffectsOnMiss(actingSide, otherSide)
            return messages
          
        # Do damage
        message = self.damageDelegate.doDamage(actingSide, otherSide)
        if message and len(message) is not 0:
            messages = messages + message      
        
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
        
    def checkPreConditions(self, actingSide, otherSide):
        """ Checks all pre-conditions to the Battle """
        messages = []
        for condition in self.conditionsToCheck:
            stop, message = condition(actingSide, otherSide)
            messages = messages + message
            if stop:
                return stop, messages
        
        return False, messages
        
    def checkLock(self, actingSide, otherSide):
        """ Checks if the user has acquired a lock during this turn
        If so, use the lock """
        if actingSide.trainer.actionLock and \
                hasattr(actingSide.trainer.actionLock.action, "attack") and \
                actingSide.trainer.actionLock.action.attack is not self:
            messages = actingSide.trainer.actionLock.attack.use(actingSide, otherSide)
            return True, messages
        return False, []
        
        
    def checkFlinch(self, actingSide, otherSide):
        """ Checks if the actor is flinching """
        if actingSide.flinching:
            return True, [actingSide.getHeader() + " flinched."]
        return False, []
        
    def checkCharging(self, actingSide, otherSide):
        """ Checks if the user's attack requires charging on this turn """
        for effect in self.effectDelegates:
            if hasattr(effect, "isCharging") and effect.isCharging(actingSide):
                return True, [actingSide.getHeader() + effect.message]
                
        return False, []
        
    def checkEncore(self, actingSide, otherSide):
        """ Checks if the user is being forced to encore """
        if actingSide.encore > 0:
            actingSide.encore = actingSide.encore - 1
        return False, []
        
    def checkStatus(self, actingSide, otherSide):
        """ Checks if the user's status prevents a move this turn """
        return actingSide.currPokemon.getStatus().immobilized(actingSide)
        
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