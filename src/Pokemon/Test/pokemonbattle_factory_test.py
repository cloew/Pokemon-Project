import unittest
from Test.test_helper import *

class functionToTest(unittest.TestCase):
    """ Test cases of functionToTest """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def caseToTest(self):
        """ Test that ... """

# Collect all test cases in this class
testcasesFunctionToTest = ["caseToTest"]
suiteFunctionToTest = unittest.TestSuite(map(functionToTest, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()