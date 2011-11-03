from Battle.Status.status import Status

class CureStatusDelegate(object):
    """ Represents an effect that cures a status ailment """
    
    def __init__(self, status, affectUser):
        """ Builds the CureStatusDelegate from the status it cures and which it side it cures """
        self.status = status
        self.affectUser = affectUser
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the deleagte's effect """
        if self.affectUser:
            return self.checkCurable(actingSide)
        else:
            return self.checkCurable(otherSide)
        
    def checkCurable(self, side):
        """ Checks if the status is curable """
        messages = []
        if self.status == side.currPokemon.getStatus().abbr:
            messages = self.cureStatus(side)
        
        return messages
        
    def cureStatus(self, side):
        """ Cures the status from the active pokemon on the given side """
        status = side.currPokemon.getStatus()
        messages = status.getDoneMessage(side)
        side.currPokemon.setStatus(Status())
        return messages