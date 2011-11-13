from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class AlwaysHitDelegate(HitDelegate):
  """ Represents an Attack's ability to hit an opponent """
  accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 9,
                   1/3.0, 3/8.0, .428, 1/2.0, 3/5.0, 3/4.0]
  
  def __init__(self):
    """ Build a core hit Delegate """
    
    
  def hit(self, actingSide, otherSide):
    """ Returns true, always hits, unless other circumstances """
    return not self.dodging(otherSide), [self.message]