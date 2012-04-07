import unittest
from Test.test_helper import *

from Battle.Attack.EffectDelegates.multi_turn_range_delegate import MultiTurnRangeDelegate

class Init(unittest.TestCase):
    """ Test cases of __init__ """
    
    def  setUp(self):
        """ Build the Effect for the test """
        self.min = 1
        self.max = 1
        
        self.delegate = MultiTurnRangeDelegate(self.min, self.max, None)
        
    def turns(self):
        """ Test that turns is within min and max """
        assert self.delegate.turns in range(self.min, self.max+1), "Turns should be between max and min"

# Collect all test cases in this class
testcasesInit = ["turns"]
suiteInit = unittest.TestSuite(map(Init, testcasesInit))

##########################################################

class resetTurns(unittest.TestCase):
    """ Test cases of resetTurns """
    
    def  setUp(self):
        """ Build the Delegate for the test """
        self.min = 1
        self.max = 10
        
        self.delegate = MultiTurnRangeDelegate(self.min, self.max, None)
        
    def turnOn(self):
        """ Test that turnOn is reset """
        self.delegate.turnOn = 1
        self.delegate.resetTurns()
        assert  self.delegate.turnOn == 0, "Turn On should be reset"
        
    def turns(self):
        """ Test that turns is reset to within the min and max """
        self.delegate.resetTurns()
        assert self.delegate.turns in range(self.min, self.max+1), "Turns should be between max and min"

# Collect all test cases in this class
testcasesResetTurns = ["turnOn", "turns"]
suiteResetTurns = unittest.TestSuite(map(resetTurns, testcasesResetTurns))

##########################################################

# Collect all test cases in this file
suites = [suiteInit, suiteResetTurns]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()