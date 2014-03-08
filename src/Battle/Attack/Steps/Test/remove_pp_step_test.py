from Battle.Attack.attack import Attack
from Battle.Attack.HitDelegates.hitself_delegate import HitSelfDelegate
from Battle.Attack.Steps.remove_pp_step import RemovePPStep

from Test.test_helper import BuildPokemonBattleWrapper
import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.originalPowerPointsValue = 10
        self.attack.currPowerPoints = self.originalPowerPointsValue
        self.step = RemovePPStep(self.attack)
        self.target = BuildPokemonBattleWrapper()
        self.target.getAbility().powerPointsPressure = self.powerPointsPressure
        
        self.pressure = 2
        self.usedAbility = False
        
    def standard(self):
        """ Test that the PP is decreased under normal circumstances """
        ppValue = 10
        self.attack.currPowerPoints = ppValue
        
        self.step.perform(None, self.target, None)
        
        self.assertTrue(self.usedAbility, "PP Pressure should have been determined by the Target's Pressure")
        self.assertEquals(ppValue-self.pressure, self.attack.currPowerPoints, "PP should have been reduced by the Target's Pressure")
        
    def hitSelf(self):
        """ Test that the PP is decreased under normal circumstances """
        self.attack.hitDelegate = HitSelfDelegate()
        ppValue = 10
        self.attack.currPowerPoints = ppValue
        
        self.step.perform(None, self.target, None)
        
        self.assertFalse(self.usedAbility, "PP Pressure should not have been determined by the Target's Pressure")
        self.assertEquals(ppValue-1, self.attack.currPowerPoints, 'PP should have been reduced by 1')
        
    def zero(self):
        """ Test that the PP is not decreased when already at zero """
        ppValue = 0
        self.attack.currPowerPoints = ppValue
        
        self.step.perform(None, self.target, None)
        
        self.assertEquals(0, self.attack.currPowerPoints, 'PP should stay at 0')
        
    def powerPointsPressure(self):
        """ Return the power Point Pressure """
        self.usedAbility = True
        return self.pressure

# Collect all test cases in this class
testcasesPerform = ["standard", "hitSelf", "zero"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)