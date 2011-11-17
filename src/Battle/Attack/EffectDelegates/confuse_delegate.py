from Battle.SecondaryEffects.confusion import Confusion

class ConfuseDelegate :
    """ Represents an effect that confuses the opponent """
    
    def __init__(self, affectUser):
        """ Build the Confuse Delegate """
        self.affectUser = affectUser
        
    def getTargetSide(self, actingSide, otherSide):
        """ Returns the side that is affected """
        if self.affectUser:
            return actingSide
        else:
            return otherSide
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the Confusion to the target """
        side = self.getTargetSide(actingSide, otherSide)
        message = side.getHeader()
        
        if not self.isConfused(side):
            side.secondaryEffects.append(Confusion())
            message = message + Confusion.start
        else:
            message = message + Confusion.already
            
        return [message]
                
    def isConfused(self, side):
        """ Returns if the side is already confused """
        for effect in side.secondaryEffects:
            if effect.__class__ == Confusion:
                return True
                
        return False 