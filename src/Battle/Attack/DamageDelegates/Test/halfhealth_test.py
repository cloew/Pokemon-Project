import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.halfhealth_delegate import HalfHealthDelegate

class calcDamage(unittest.TestCase):
    """ Test cases of calcDamage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.delegate = HalfHealthDelegate(None, 1)
        
    def halfHealth(self):
        """ Test that the damage is Half the Health of the target """
        hp = 100
        self.target.setCurrHP(hp)
        
        damage = self.delegate.calcDamage(self.user, self.target)
        assert damage == hp/2, "Damage should be half the targets health"
        
    def halfHealthNotFloored(self):
        """ Test that the damage is Half the Health of the target """
        hp = 101
        self.target.setCurrHP(hp)
        
        damage = self.delegate.calcDamage(self.user, self.target)
        assert damage == hp/2.0, "Damage should be half the targets health, not floored"

# Collect all test cases in this class
testcasesCalcDamage = ["halfHealth", "halfHealthNotFloored"]
suiteCalcDamage = unittest.TestSuite(map(calcDamage, testcasesCalcDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteCalcDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()