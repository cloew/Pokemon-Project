import unittest
from Test.test_helper import *

from Battle.Attack.EffectDelegates.multi_turn_fixed_delegate import FixedMultiTurnDelegate

class Init(unittest.TestCase):
    """ Test cases of __init__ """
    
    def  setUp(self):
        """ Build the Effect for the test """
        self.turns = 2
        self.delegate = FixedMultiTurnDelegate(self.turns, None)
        
    def turns(self):
        """ Test that turns is set """
        assert self.delegate.turns == self.turns, "Turns should be set"

# Collect all test cases in this class
testcasesInit = ["turns"]
suiteInit = unittest.TestSuite(map(Init, testcasesInit))

##########################################################

# Collect all test cases in this file
suites = [suiteInit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()