import unittest
from Test.test_helper import *

from Battle.battle_message import BattleMessage

class getMessageSlice(unittest.TestCase):
    """ Test cases of getMessageSlice """
    MESSAGE_STR = "1234567890"
    
    def  setUp(self):
        """ Build the BattleMessage for the test """
        self.message = BattleMessage(self.MESSAGE_STR)
        
    def slice(self):
        """ Test that a slice of the Battle Message is returned properly """
        sliceIndex = 2
        originalSlice = self.MESSAGE_STR[:sliceIndex]
        messageSlice = self.message.getMessageSlice(sliceIndex)
        
        assert originalSlice == messageSlice, "Message slice does not match the slice from the original string"
        assert not self.message.fullyDisplayed, "Message should not have fullyDisplayed"
        
    def fullMessage(self):
        """ Test that a slice of the Battle Message is returned properly """
        sliceIndex = len(self.MESSAGE_STR)
        originalSlice = self.MESSAGE_STR[:sliceIndex]
        messageSlice = self.message.getMessageSlice(sliceIndex)
        
        assert originalSlice == messageSlice, "Message slice should be the original string"
        assert self.message.fullyDisplayed, "Message should have fullyDisplayed"

# Collect all test cases in this class
testcasesGetMessageSlice = ["slice", "fullMessage"]
suiteGetMessageSlice = unittest.TestSuite(map(getMessageSlice, testcasesGetMessageSlice))

##########################################################

# Collect all test cases in this file
suites = [suiteGetMessageSlice]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()