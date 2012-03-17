import unittest
from Test.test_helper import *

from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class cantHandle(unittest.TestCase):
    """ Test cases of cantHandle """
    
    def  setUp(self):
        """ Build the FaintHandler for the test """
        self.handler = FaintHandlerDelegate()
        
    def regardless(self):
        """ Test that it returns false regardless """
        cantHandle = self.handler.cantHandle()
        assert not cantHandle, "Can handle"

# Collect all test cases in this class
testcasesCantHandle = ["regardless"]
suiteCantHandle = unittest.TestSuite(map(cantHandle, testcasesCantHandle))

##########################################################

# Collect all test cases in this file
suites = [suiteCantHandle]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()