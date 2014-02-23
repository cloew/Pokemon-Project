from Battle.Attack.Steps.attack_step import AttackStep

class HitStep(AttackStep):
    """ Represents the Hit Step in performing an Attack """
    
    def __init__(self, parent):
        """ Initialize the Precondition Step """
        AttackStep.__init__(self, parent)
        self.hit = False
        
    def perform(self, user, target, environment):
        """ Perform this step """
        self.hit, messages = self.parent.hitDelegate.hit(user, target, environment)
        if not self.hit:
            return messages
        else:
            return []