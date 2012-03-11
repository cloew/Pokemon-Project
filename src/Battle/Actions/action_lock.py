
class ActionLock:
    """ Represents an action that will continued for some number of turns """
    
    def __init__(self, parent, action, turnsToLast):
        """ Builds an action, giving it the action to continue and the number of turns to keep going """
        self.parent = parent
        self.action = action
        self.turnsToGo = turnsToLast
        
    def useAction(self):
        """ Returns the action for use and decrements the counter """
        self.turnsToGo -= 1
        if self.done():
            self.parent.actionLock = None
        return self.action
        
    def done(self):
        """ Returns whether the lock has depleted """
        return (self.turnsToGo == 0)