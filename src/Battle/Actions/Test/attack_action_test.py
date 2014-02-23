import unittest

from Battle.Actions.attack_action import AttackAction
from Battle.Attack.attackfactory import AttackFactory

class getPriority(unittest.TestCase):
    """ Test cases of getPriority """
    
    def  setUp(self):
        """ Build the Attack Action """
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.priority = attack.speedDelegate.priority
        self.action = AttackAction(attack, None, None, None)
        
    def priorityIsCorrect(self):
        """ Test that the priority is returned correctly """
        assert self.action.getPriority() == self.priority, "Priority should be the priority of the attack provided"

# Collect all test cases in this class
testcasesGetPriority = ["priorityIsCorrect"]
suiteGetPriority = unittest.TestSuite(map(getPriority, testcasesGetPriority))

##########################################################

class doAction(unittest.TestCase):
    """ Test cases of doAction """
    
    def  setUp(self):
        """ Build the Attack Action """
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.priority = attack.speedDelegate.priority
        attack.use = self.use
        self.action = AttackAction(attack, None, None, None)
        self.usedAttack = False
        
    def attackUsed(self):
        """ Test that the wrapped attack is used """
        self.action.doAction()
        assert self.usedAttack, "Should have used the Action's Attack"
        
    def use(self, user, target, environment):
        self.usedAttack = True

# Collect all test cases in this class
testcasesDoAction = ["attackUsed"]
suiteDoAction = unittest.TestSuite(map(doAction, testcasesDoAction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetPriority, suiteDoAction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()