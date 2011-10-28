import unittest

from Battle.Actions.attack_action import AttackAction
from Battle.Attack.attackfactory import AttackFactory

class getPriority(unittest.TestCase):
    """ Test cases of getPriority """
    
    def  setUp(self):
        """ Build the Attack Action """
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.priority = attack.speedDelegate.priority
        self.action = AttackAction(attack)
        
    def priorityIsCorrect(self):
        """ Test that the priority is returned correctly """
        assert self.action.getPriority() == self.priority, "Priority should be the priority of the attack provided"

# Collect all test cases in this class
testcasesGetPriority = []
suiteGetPriority = unittest.TestSuite(map(getPriority, testcasesGetPriority))

##########################################################
# Collect all test cases in this file
suites = [suiteGetPriority]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()