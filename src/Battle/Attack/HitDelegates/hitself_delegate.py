from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class HitSelfDelegate(HitDelegate):
    """ Represents an Attack that affects either the environment or ithe user 
    So, it is always able to hit """
    accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 9,
                   1/3.0, 3/8.0, .428, 1/2.0, 3/5.0, 3/4.0]
                   
    def __init__(self):
        """ Builds an self hit delegate with no parameters """
    
    # Will incorporate into the default hit
    # When user is target, automatically hits
    def hit(self, user, target):
        """ Returns true, always hits, unless other circumstances """
        return True, []