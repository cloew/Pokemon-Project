import unittest
#from Test.test_helper import *

from Battle.Attack.EffectDelegates.useless_delegate import UselessDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.delegate = UselessDelegate()
        
    def message(self):
        """ Test that the message is correct """
        messages = self.delegate.applyEffect(None, None, None)
        assert messages == [UselessDelegate.message], "Should have a message saying the attack was useless"

# Collect all test cases in this class
testcasesApplyEffect = ["message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()