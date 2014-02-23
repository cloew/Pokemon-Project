from Battle.Attack.preconditions import PreconditionChecker
from Battle.Attack.Steps.attack_step import AttackStep

class PreconditionStep(AttackStep):
    """ Represents the Precondition Step in performing an Attack """
    
    def __init__(self, parent):
        """ Initialize the Precondition Step """
        AttackStep.__init__(self, parent)
        self.stop = True
        
    def perform(self, user, target, environment, PreconditionChecker=PreconditionChecker):
        """ Perform this step """
        preconditionChecker = PreconditionChecker(user, target, environment, self.parent)
        self.stop, messages = preconditionChecker.checkPreConditions()
        
        return messages
        
    @property
    def passed(self):
        """ Return if the Precondition Step Passed """
        return not self.stop