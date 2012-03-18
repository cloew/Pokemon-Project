
class PreconditionChecker:
    """ Class that checks all preconditions """
    
    
    def __init__(self, user, target, attack):
        """ Builds an object to check preconditions """
        self.user = user
        self.target = target
        self.attack = attack
        
        self.conditionsToCheck = [self.checkFaint, self.checkLock, self.checkFlinch, self.checkCharging,
                                              self.checkAbility, self.checkEncore, self.checkStatus, self.checkSecondaries]
        
    def checkPreConditions(self):
        """ Checks all pre-conditions to the Battle """
        messages = []
        afterCharge = False
        
        for condition in self.conditionsToCheck:
            stop, message = condition()
            messages = messages + message
            
            if condition == self.checkAbility:
                afterCharge = True
                
            if stop:
                if afterCharge:
                    for effect in self.attack.effectDelegates:
                        effect.stopCharge(self.user)
                return stop, messages
        
        return False, messages
        
    def checkFaint(self):
        """ Checks if the using Pkmn had fainted """
        if self.user.fainted():
            return True, []
        return False, []
        
    def checkLock(self):
        """ Checks if the user has acquired a lock during this turn
        If so, use the lock """
        if self.user.actionLock and \
                hasattr(self.user.actionLock.action, "attack") and \
                self.user.actionLock.action.attack is not self.attack:
            messages = self.user.actionLock.useAction().doAction()  # This needs to be looked at... # VERY needs to be looked at
            return True, messages
        return False, []
        
    def checkFlinch(self):
        """ Checks if the user is flinching """
        if self.user.flinching:
            return True, [self.user.getHeader() + " flinched."]
        return False, []
        
    def checkCharging(self):
        """ Checks if the user's attack requires charging on this turn """
        for effect in self.attack.effectDelegates:
            if hasattr(effect, "isCharging") and effect.isCharging(self.user):
                self.user.getAbility().onCharge()
                return True, [self.user.getHeader() + effect.message]
                
        return False, []
        
    def checkAbility(self):
        """ Checks if the Ability prevents the user from attacking """
        return self.user.getAbility().stopAttack(self.user)
        
    def checkEncore(self):
        """ Checks if the user is being forced to encore """
        if self.user.encore > 0:
            self.user.encore = self.user.encore - 1
        return False, []
        
    def checkStatus(self):
        """ Checks if the user's status prevents a move this turn """
        return self.user.getStatus().immobilized(self.user)
        
    def checkSecondaries(self):
        """ Checks if the user's secondary effects prevent a move this turn """
        allMessages = []
        for effect in self.user.secondaryEffects:
            stop, messages = effect.immobilized(self.user)
            allMessages = allMessages + messages
            if stop:
                return stop, allMessages
        return False, allMessages
        