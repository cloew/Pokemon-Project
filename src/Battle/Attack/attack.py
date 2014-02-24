from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

from Battle.Attack.Steps.announcement_step import AnnouncementStep
from Battle.Attack.Steps.damage_step import DamageStep
from Battle.Attack.Steps.effects_step import EffectsStep
from Battle.Attack.Steps.handle_contact_step import HandleContactStep
from Battle.Attack.Steps.handle_miss_effects_step import HandleMissEffectsStep
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
        self.makes_contact = False
        self.powerPoints = 0
        self.currPowerPoints = 0
        
        self.preconditionsStep = PreconditionStep(self)
        self.announcementStep = AnnouncementStep(self)
        self.hitStep = HitStep(self)
        self.damageStep = DamageStep(self)
        self.effectsStep = EffectsStep(self)
        self.handleContactStep = HandleContactStep(self)
        self.handleMissEffectsStep = HandleMissEffectsStep(self)
        
    def use(self, user, target, environment):
        """ Uses the current attack Object in a Battle """
        messages = []
        messages += self.preconditionsStep.perform(user, target, environment)
        if self.preconditionsStep.passed:
            messages += self.announcementStep.perform(user, target, environment)
            messages += self.hitStep.perform(user, target, environment)
            if self.hitStep.hit:
                messages += self.damageStep.perform(user, target, environment)
                messages += self.effectsStep.perform(user, target, environment)
                messages += self.handleContactStep.perform(user, target, environment)
            else:
                messages += self.handleMissEffectsStep.perform(user, target, environment)
        
        return messages
        
    # Helper Methods
    def addDelegate(self, delegateCategory, delegate):
        """ Adds a delegate to an Attack Object """
        if delegateCategory == Tags.effectDelegateTag:
            self.effectDelegates.append(delegate)
            return
        setattr(self, delegateCategory, delegate)
        
    def isStatus(self):
        """ Returns if the Attack is a status attack """
        return isinstance(self.damageDelegate, NullDamageDelegate)