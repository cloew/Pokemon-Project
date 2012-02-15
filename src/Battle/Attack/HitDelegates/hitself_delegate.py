from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class HitSelfDelegate(HitDelegate):
    """ Represents an Attack that affects either the environment or ithe user 
    So, it is always able to hit """
                   
    def __init__(self):
        """ Builds an self hit delegate with no parameters """
    
    # Will incorporate into the default hit
    # When user is target, automatically hits
    def hit(self, user, target):
        """ Returns true, always hits, period """
        return True, []