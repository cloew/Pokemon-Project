from Battle.Attack.DamageDelegates.damagescale_delegate import DamageScaleDelegate

import unittest

class getScale(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.factor = 2
        self.delegate = DamageScaleDelegate(None, 50, 1, self.factor, 5)
        
    def correctScale(self):
        """ Test that getScale returns the correct scale """
        self.delegate.turnsToGo = 0
        scale = self.delegate.getScale()
        assert scale == 1, "Scale should be 1 when turnsToGo is 0"
        
    def correctScaleAfterInc(self):
        """ Test that scale returns correctly after the turn increments """
        self.delegate.turnsToGo = 0
        scale = self.delegate.getScale()
        
        self.delegate.incTurns()
        scale2 = self.delegate.getScale()
        
        assert scale == scale2/self.factor, "Scale should be half of the scale when turnsToGo is 0"

# Collect all test cases in this class      
testcasesGetScale = ["correctScale", "correctScaleAfterInc"]
suiteGetScale = unittest.TestSuite(map(getScale, testcasesGetScale))

#########################################################

suites = [suiteGetScale]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()