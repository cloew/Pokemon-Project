from Battle.Attack.preconditions import PreconditionChecker

class PreconditionStep:
    """ Represents the Precondition Step in performing an Attack """
    
    def __init__(self, parent):
        """ Initialize the Precondition Step """
        self.parent = parent
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