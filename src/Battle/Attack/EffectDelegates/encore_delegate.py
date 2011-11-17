
class EncoreDelegate:
    """ Represents an attack that is locked for some number of future turns """
    
    def __init__(self, turns, affectUser):
        """ Builds a ChanceDelegate """
        self.turns = turns
        self.affectUser = affectUser
        
    def getTargetSide(self, actingSide, otherSide):
        """ Returns the side that is affected """
        if self.affectUser:
            return actingSide
        else:
            return otherSide
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegates effect """
        message = []
        side = getTargetSide(actingSide, otherSide)
        
        if self.immune(actingSide, otherSide):
            side.encore = self.turns
        else:
            message = []
                
        return message
        
    def immune(self, actingSide, otherSide):
        """ Returns if the target is immune to the attack """
        return True # This attack is going to be more troublesome
                            # Have to keep track of target and the like as well
                            # Just gonna save this for after I've added the PkmnWrapper Class
        side = getTargetSide(actingSide, otherSide)
        return side.lastAction and hasattr(side.lastAction, "attack")