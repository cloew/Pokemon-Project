from Battle.Attack.attack import Attack
from Battle.Attack.Steps.damage_step import DamageStep

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.attack.damageDelegate = self
        self.step = DamageStep(self.attack)
        
        self.messages = ["My Test Messages"]
        self.calledDoDamage = False
        
    def usedDamageDelegate(self):
        """ Test that failing hit is handled """
        self.step.perform(None, None, None)
        
        self.assertTrue(self.calledDoDamage, "Should have called damage delegate's damage function")
    
    def messagesReturned(self):
        """ Test that messages from a missed hit attempt are returned """
        messages = self.step.perform(None, None, None)
        
        self.assertEquals(self.messages, messages, "Should have returned the damage messages")
        
    def doDamage(self, user, target, environment):
        self.calledDoDamage = True
        return self.messages

# Collect all test cases in this class
testcasesPerform = ["usedDamageDelegate", "messagesReturned"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)