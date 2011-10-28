
class SelfDestructDelegate:
    """ Represents a self-destruct effect on an Attack """
    
    def __init__(self):
        """ Builds a self-destruct delegate """
        self.applyOnMiss = 1
        
    def applyEffect(self, actingSide, otherSide):
        """ Apply the recoil effect """
        user = actingSide.currPokemon
        totake = user.battleDelegate.currHP
        user.battleDelegate.takeDamage(totake)
        
        return [user.name + " self-destructed."]