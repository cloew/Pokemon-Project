from Battle.Actions.switch_action import SwitchAction

import unittest

class getPriority(unittest.TestCase):
    """ Test cases of getPriority """
    
    def  setUp(self):
        """ Build the Switch Action for the test """
        self.action = SwitchAction(None, None)
        
    def switchValue(self):
        """ Test that the priority returned is the Switch Action Priority """
        priority = self.action.getPriority()
        self.assertEquals(priority, SwitchAction.PRIORITY, "Priority should be the Switch Action Priority")

# Collect all test cases in this class
testcasesGetPriority = ["switchValue"]
suiteGetPriority = unittest.TestSuite(map(getPriority, testcasesGetPriority))

##########################################################

class doAction(unittest.TestCase):
    """ Test cases of doAction """
    
    def  setUp(self):
        """ Build the Switch Action for the test """
        self.action = SwitchAction(self, None)
        self.calledSendOutPkmn = False
        
    def sendOutPkmnCalled(self):
        """ Test that the priority returned is the Switch Action Priority """
        self.action.doAction()
        self.assertTrue(self.calledSendOutPkmn, "Should have called the sendOutPkmn method")
        
    def sendOutPkmn(self, pkmnToSwitchTo):
        self.calledSendOutPkmn = True

# Collect all test cases in this class
testcasesDoAction = ["sendOutPkmnCalled"]
suiteDoAction = unittest.TestSuite(map(doAction, testcasesDoAction))

##########################################################

# Collect all test cases in this file
suites = [suiteGetPriority, suiteDoAction]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)