from Battle.Attack.attack import Attack
from Battle.Attack.Steps.hit_step import HitStep

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.attack.hitDelegate = self
        self.step = HitStep(self.attack)
        
        self.messages = ["My Test Messages"]
        self.calledHit = False
        
    def hit_Failing(self):
        """ Test that failing hit is handled """
        self.shouldHit = False
        self.step.perform(None, None, None)
        
        self.assertTrue(self.calledHit, "Should have called hit delegate's hit function")
        self.assertFalse(self.step.hit, "Should not have successfully hit")
        
    def hit_Passing(self):
        """ Test that passing hit ais handled """
        self.shouldHit = True
        self.step.perform(None, None, None)
        
        self.assertTrue(self.calledHit, "Should have called hit delegate's hit function")
        self.assertTrue(self.step.hit, "Should have successfully hit")
    
    def messagesReturned(self):
        """ Test that messages from the hit attempt are returned """
        self.shouldHit = True
        messages = self.step.perform(None, None, None)
        
        self.assertEquals(self.messages, messages, "Should have returned the hit messages")
        
    def hit(self, user, target, environment):
        self.calledHit = True
        return self.shouldHit, self.messages

# Collect all test cases in this class
testcasesPerform = ["hit_Failing", "hit_Passing", "messagesReturned"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)