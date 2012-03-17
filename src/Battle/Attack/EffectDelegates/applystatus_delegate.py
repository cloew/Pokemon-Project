from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate
from Battle.Status.statusfactory import StatusFactory

class ApplyStatusDelegate(EffectDelegate):
    """ Represents an effect that applies a status """
    
    def __init__(self, parent, status, affectUser):
        """ Build the status """
        self.parent = parent
        self.status = status
        self.affectUser = affectUser
        
    def applyEffect(self, user, target):
        """ Applies the status to one side based on affectUser """
        pkmn = self.getEffectedPokemon(user, target)
        messages = self.applyStatus(pkmn)
            
        return messages
        
    def applyStatus(self, pkmn):
        """ Applies the given status to the given Pokemon """
        status, message = StatusFactory.buildStatusFromAbbr(self.status)
        
        if self.checkImmune(status, pkmn):
            return []
        if self.checkStatusAlready(pkmn):
            return []
        
        pkmn.setStatus(status)
        messages = [pkmn.getHeader() + message]
        
        message = pkmn.getAbility().onStatus(pkmn, status)
        messages = messages + message
        
        return messages
        
    def immune(self, user, target):
        """ Checks if the target is immune to the status effect """
        status, message = StatusFactory.buildStatusFromAbbr(self.status)
        pkmn = self.getEffectedPokemon(user, target)
        
        return self.checkImmune(status, pkmn) or self.checkStatusAlready(pkmn)
        
    def checkImmune(self, status, pkmn):
        """ Returns if the target is immune to the status effect """
        return status.immune(pkmn.getTypes(), self.parent.type)
        
    def checkStatusAlready(self, pkmn):
        """ Returns if the pokemon already has a status """
        return not pkmn.getStatus().abbr.isspace()