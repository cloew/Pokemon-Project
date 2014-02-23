import random

class BattleAction:
    """ Represents an action in a Battle """
    
    def __init__(self, user, priority):
        """ Builds a Battle Action """
        self.user = user
        self.priority = priority
    
    def getPriority(self):
        """ Returns the Speed Priority of the Action """
        return self.priority
        
    def doAction(self):
        """ Performs the action """
        return 
        
    def __cmp__(self, other):
        """ Compare an action to another """
        if not hasattr(other, "getPriority"):
            return NotImplemented
            
        return self.comparePriority(other)
                
    def comparePriority(self, other):
        """ Compares Prioirty to determine who has priority 
             NOTE: Never returns 0
             If the priorities are equal it checks the actions speeds """
        cmp =  self.getPriority().__cmp__(other.getPriority())
        if cmp == 0:
            cmp = self.compareSpeed(other)
        return cmp
            
    def compareSpeed(self, other, random=random):
        """ Compares Speed to determine who has priority 
             NOTE: Never returns 0
             If the speeds are equal one is randomly chosen as greater """
        selfSpeed = int(self.user.getStat("SPD"))
        otherSpeed = int(other.user.getStat("SPD"))
        
        cmp =  selfSpeed.__cmp__(otherSpeed)
        if cmp == 0:
            cmp = random.randrange(-1, 2, 2) # Returns -1 or 1
        return cmp