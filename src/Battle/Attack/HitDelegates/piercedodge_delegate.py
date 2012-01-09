from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class PierceDodgeDelegate(HitDelegate):
    """ Represents an attack that pierces a certain kind of dodge """
    
    def __init__(self, parent, toHit, pierce):
        """ Build a core hit Delegate """
        self.parent = parent
        self.chanceToHit = toHit
        self.pierce = pierce
        
    def dodging(self, target):
        """ Returns if the opp is dodging the current attack """
        dodging = super(PierceDodgeDelegate, self).dodging(target)
        
        if dodging and target.dodge != self.pierce:
            return True
        else:
            return False 