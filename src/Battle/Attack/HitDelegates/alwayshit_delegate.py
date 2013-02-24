from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class AlwaysHitDelegate(HitDelegate):
  """ Represents an Attack's ability to hit an opponent """
  
  def __init__(self, message):
    """ Build a Always Hit Delegate """
    self.message = message
    self.chanceToHit = 100
    
  def checkHit(self, user, target, environment):
    """ Returns true, always hits """
    return True
    