from Battle.Attack.attack import Attack
from Battle.Attack.Steps.remove_pp_step import RemovePPStep

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.originalPowerPointsValue = 10
        self.attack.currPowerPoints = self.originalPowerPointsValue
        self.step = RemovePPStep(self.attack)
        
    def standard(self):
        """ Test that the PP is decreased under normal circumstances """
        ppValue = 10
        self.attack.currPowerPoints = ppValue
        
        self.step.perform(None, None, None)
        
        self.assertEquals(ppValue-1, self.attack.currPowerPoints, 'PP should have been reduced by 1')
        
    def zero(self):
        """ Test that the PP is not decreased when already at zero """
        ppValue = 0
        self.attack.currPowerPoints = ppValue
        
        self.step.perform(None, None, None)
        
        self.assertEquals(0, self.attack.currPowerPoints, 'PP should stay at 0')

# Collect all test cases in this class
testcasesPerform = ["standard", "zero"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)