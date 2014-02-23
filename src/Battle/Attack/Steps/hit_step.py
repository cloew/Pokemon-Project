
class HitStep:
    """ Represents the Hit Step in performing an Attack """
    
    def __init__(self, parent):
        """ Initialize the Precondition Step """
        self.parent = parent
        self.hit = False
        
    def perform(self, user, target, environment):
        """ Perform this step """
        self.hit, messages = self.parent.hitDelegate.hit(user, target, environment)
        return messages