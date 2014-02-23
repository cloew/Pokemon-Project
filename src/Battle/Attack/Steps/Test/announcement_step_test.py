from Battle.Attack.attack import Attack
from Battle.Attack.Steps.announcement_step import AnnouncementStep

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.attack.name = "Test Attack"
        self.step = AnnouncementStep(self.attack)
        
        self.header = "Header"
        self.calledGetHeader = False
        
    def announcementCreated(self):
        """ Test that the announcement message was created """
        messages = self.step.perform(self, None, None)
        
        self.assertEquals(1, len(messages), "Should have a single message")
        self.assertTrue(self.calledGetHeader, "Should have used the user getHeader function")
        self.assertIn(self.header, messages[0], "Should contain the user header")
        self.assertIn(self.attack.name, messages[0], "Should contain the attack name")
        
    def getHeader(self):
        self.calledGetHeader = True
        return self.header

# Collect all test cases in this class
testcasesPerform = ["announcementCreated"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)