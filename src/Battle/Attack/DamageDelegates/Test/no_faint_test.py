import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.no_faint_delegate import NoFaintDelegate

class normalize(unittest.TestCase):
    """ Tests that Normalize normalizes correctly """
    
    def setUp(self):
        """ Build the Damage Delegate """
        self.target = BuildPokemonBattleWrapper()
        self.delegate = NoFaintDelegate(None, 0, 1)
        
    def lessThanTargetHP(self):
        """ Test that damage is normalized correctly when less than the target's HP """
        damage = self.target.getCurrHP()-1
        newDamage = self.delegate.normalize(damage, self.target)
        assert newDamage == damage, "Should return the original damage"
        
    def targetHP(self):
        """ Test that damage is normalized correctly when equal to the target's HP """
        damage = self.target.getCurrHP()
        newDamage = self.delegate.normalize(damage, self.target)
        assert newDamage == self.target.getCurrHP() -1 , "Should return one less than the target's HP as damage"
        
    def greaterThanTargetHP(self):
        """ Test that damage is normalized correctly when greater than the target's HP """
        damage = self.target.getCurrHP()+1
        newDamage = self.delegate.normalize(damage, self.target)
        assert newDamage == self.target.getCurrHP() -1, "Should return one less than the target's HP as damage"

# Collect all test cases in this class      
testcasesNormalize = ["lessThanTargetHP", "targetHP", "greaterThanTargetHP"]
suiteNormalize  = unittest.TestSuite(map(normalize , testcasesNormalize ))
        
#########################################################

# Collect all test cases in this file
suites = [suiteNormalize]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()