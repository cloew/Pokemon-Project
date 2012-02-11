import unittest

from Battle.Attack.EffectDelegates.chance_delegate import ChanceDelegate

class shouldApply(unittest.TestCase):
    """ Test cases of shouldApply """
    
    def  setUp(self):
        """ Build the Delegate for the test """
        self.delegate = ChanceDelegate(0, [])
        
    def should(self):
        """ Test that the effect should be applied if the chance is higher """
        self.delegate.chance = 70
        should = self.delegate.shouldApply(20)
        assert should, "The effect should be applied"
        
    def shouldNot(self):
        """ Test that the effect should not be applied if the chance is lower """
        self.delegate.chance = 20
        should = self.delegate.shouldApply(70)
        assert not should, "The effect should not be applied"

# Collect all test cases in this class
testcasesShouldApply = ["should", "shouldNot"]
suiteShouldApply = unittest.TestSuite(map(shouldApply, testcasesShouldApply))

##########################################################

# Collect all test cases in this file
suites = [suiteShouldApply]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()