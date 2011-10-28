from Battle.Status.statusfactory import StatusFactory

class ApplyStatusDelegate:
    """ Represents an effect that applies a status """
    
    def __init__(self, parent, status, affectUser):
        """ Build the status """
        self.parent = parent
        self.status = status
        self.affectUser = affectUser
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the status to one side based on affectUser """
        if self.affectUser:
            messages = self.applyStatus(actingSide)
        else:
            messages = self.applyStatus(otherSide)
            
        return messages
        
    def applyStatus(self, side):
        """ Applies the given status to the Pokemon on the given side """
        status, message = StatusFactory.buildStatusFromAbbr(self.status)
        
        if self.checkImmune(status, side):
            return []
        if self.checkStatusAlready(side):
            return []
        
        side.currPokemon.setStatus(status)
        message = side.currPokemon.name + message
        
        return [message]
        
    def checkImmune(self, status, side):
        """ Returns if the target is immune to the status effect """
        return status.immune(side.currPokemon.getTypes(), self.parent.type)
        
    def checkStatusAlready(self, side):
        """ Returns if the pokemon already has a status """
        return not side.currPokemon.getStatus().abbr.isspace()