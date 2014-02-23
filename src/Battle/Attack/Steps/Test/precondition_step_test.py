from Battle.Attack.attack import Attack
from Battle.Attack.Steps.precondition_step import PreconditionStep

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.step = PreconditionStep(self.attack)
        self.preconditionMessages = ["My Precondition Messages"]
        self.attackMessages = ["My Attack Messages"]
        
        self.calledCheckPreConditions = False
        
    def preconditions_Failing(self):
        """ Test that failing precodnitions prevents the attack from being done """
        self.failPreconditions = False
        self.step.perform(None, None, None, PreconditionChecker=self.buildPreconditionChecker)
        
        self.assertTrue(self.calledCheckPreConditions, "Should have called checkPreconditions")
        
    def preconditions_Passing(self):
        """ Test that passing precodnitions allows the attack to be used """
        self.failPreconditions = True
        self.step.perform(None, None, None, PreconditionChecker=self.buildPreconditionChecker)
        
        self.assertTrue(self.calledCheckPreConditions, "Should have called checkPreconditions")
    
    def messagesReturned(self):
        """ Test that messages from the Preconditions Checker are returned """
        self.failPreconditions = False
        messages = self.step.perform(None, None, None, PreconditionChecker=self.buildPreconditionChecker)
        
        self.assertEquals(self.preconditionMessages, messages, "Should have returned the messages from the Preconditions check")
        
    def buildPreconditionChecker(self, user, target, environment, attack):
        return self
        
    def checkPreConditions(self):
        self.calledCheckPreConditions = True
        return self.failPreconditions, self.preconditionMessages

# Collect all test cases in this class
testcasesPerform = ["preconditions_Failing", "preconditions_Passing", "messagesReturned"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)