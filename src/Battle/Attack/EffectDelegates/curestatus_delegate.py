from Battle.Status.status import Status

class CureStatusDelegate(object):
    """ Represents an effect that cures a status ailment """
    
    def __init__(self, status, affectUser):
        """ Builds the CureStatusDelegate from the status it cures and which it side it cures """
        self.status = status
        self.affectUser = affectUser
        
    def applyEffect(self, user, target):
        """ Applies the delegate's effect """
        if self.affectUser:
            return self.checkCurable(user)
        else:
            return self.checkCurable(target)
        
    def checkCurable(self, pkmn):
        """ Checks if the status is curable """
        messages = []
        if self.status == pkmn.getStatus().abbr:
            messages = self.cureStatus(pkmn)
        
        return messages
        
    def cureStatus(self, pkmn):
        """ Cures the status from the given pokemon """
        status = pkmn.getStatus()
        messages = status.getDoneMessage(pkmn)
        pkmn.setStatus(Status())
        return messages