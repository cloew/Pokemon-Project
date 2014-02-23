from Battle.Attack.preconditions import PreconditionChecker

class PreconditionStep:
    """ Represents the Precondition Step in performing an Attack """
    
    def __init__(self, parent):
        """ Initialize the Precondition Step """
        self.parent = parent
        
    def perform(self, user, target, environment, PreconditionChecker=PreconditionChecker):
        """ Perform this step """
        preconditionChecker = PreconditionChecker(user, target, environment, self.parent)
        stop, messages = preconditionChecker.checkPreConditions()
        
        if not stop:
            pass # Call Attack Announcement Step
        
        return messages