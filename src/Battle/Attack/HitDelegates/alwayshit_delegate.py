from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class AlwaysHitDelegate(HitDelegate):
  """ Represents an Attack's ability to hit an opponent """
  
  def __init__(self):
    """ Build a core hit Delegate """
    
  def checkHit(self, user, target):
    """ Returns true, always hits """
    return True
    