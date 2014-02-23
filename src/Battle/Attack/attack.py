from preconditions import PreconditionChecker

from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate
from Battle.Attack.Steps.announcement_step import AnnouncementStep
from Battle.Attack.Steps.damage_step import DamageStep
from Battle.Attack.Steps.effects_step import EffectsStep
from Battle.Attack.Steps.hit_step import HitStep
from Battle.Attack.Steps.precondition_step import PreconditionStep

from resources.tags import Tags

class Attack:
    """ Represents an Attack """
    
    def __init__(self):
        self.hitDelegate = None
        self.damageDelegate = None
        self.speedDelegate = None
        
        self.effectDelegates = []
        makes_contact = False
        
    def use(self, user, target, environment):
        """ Uses the current attack Object in a Battle """
        messages = []
        # preconditionChecker = PreconditionChecker(user, target, environment, self)
        # stop = self.checkPreconditions(preconditionChecker, messages)
        
        preconditionStep = PreconditionStep(self)
        messages += preconditionStep.perform(user, target, environment)
        
        # if not stop:
        if preconditionStep.passed:
            messages += self.doAttack(user, target, environment)
        
        return messages
        
    def doAttack(self, user, target, environment):
        """  """
        # messages = ["%s USED %s" % (user.getHeader(), self.name)]
        announcementStep = AnnouncementStep(self)
        messages = announcementStep.perform(user, target, environment)
        # hit = self.doHit(user, target, environment, messages)
        hitStep = HitStep(self)
        messages += hitStep.perform(user, target, environment)
        
        # if hit:
        if hitStep.hit:
            messages += self.doAttackLoop(user, target, environment)
        
        return messages
        
    def doAttackLoop(self, user, target, environment):
        """  """
        messages = []
        # messages += self.doDamage(user, target, environment)
        damageStep = DamageStep(self)
        messages += damageStep.perform(user, target, environment)
        # messages += self.doEffects(user, target, environment)
        effectsStep = EffectsStep(self)
        messages += effectsStep.perform(user, target, environment)
        if self.makes_contact:
            messages += target.getAbility().onContact(target, user)
        return messages
        
    # Attack Loop Functions
    def checkPreconditions(self, preconditionChecker, messages):
        """ Checks preconditions to make sure the user isn't prevented from working """
        stop, preMessages = preconditionChecker.checkPreConditions()
        messages += preMessages
        return stop
        
    def doHit(self, user, target, environment, messages):
        """ Check if the user hits the target(s) """
        hit, hitMessages = self.hitDelegate.hit(user, target, environment)
        if not hit:
            messages += hitMessages
            messages += self.applyEffectsOnMiss(user, target, environment)
        return hit
        
    def doDamage(self, user, target, environment):
        """ Does the attack's damage, returns that the loop should not stop """
        return self.damageDelegate.doDamage(user, target, environment)
        
    def doEffects(self, user, target, environment):
        """ Does the attack's effects, returns that the loop should not stop """
        messages = []

        if not self.preventEffects(user, target):
            for effect in self.effectDelegates:
                messages += effect.tryToApplyEffect(user, target, environment)
        return messages
        
    # Helper Methods
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
        
    def applyEffectsOnMiss(self, user, target, environment):
        """ Apply effects on miss """
        messages = []
        for effect in self.effectDelegates:
            if hasattr(effect, "applyOnMiss"):
                effectMessages = effect.applyEffect(user, target, environment)
                messages = messages + effectMessages
            if hasattr(effect, "effectOnMiss"):
                effectMessages = effect.effectOnMiss(user, target, environment)
                messages = messages + effectMessages
        return messages
        
    def isStatus(self):
        """ Returns if the Attack is a status attack """
        return isinstance(self.damageDelegate, NullDamageDelegate)
        