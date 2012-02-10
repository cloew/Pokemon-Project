import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.fixed_delegate import FixedDelegate

class calcDamage(unittest.TestCase):
    """ Test cases of calcDamage """
    
    def  setUp(self):
        """ Build the Delegate and Pkmn for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.damage = 40
        self.delegate = FixedDelegate(None, self.damage, 1)
        
    def fixed(self):
        """ Test that the damage returned is the fixed amount """
        self.user.statMods["ATK"] = 0
        damage =  self.delegate.calcDamage(self.user, self.target)
        assert damage == self.damage, "Damage should be the fixed amount"
        
    def fixedWithStatMod(self):
        """ Test that the damage returned is fixed even with a stat mod """
        self.user.statMods["ATK"] = 3
        damage =  self.delegate.calcDamage(self.user, self.target)
        assert damage == self.damage, "Damage should be the fixed amount"

# Collect all test cases in this class
testcasesCalcDamage = ["fixed", "fixedWithStatMod"]
suiteCalcDamage = unittest.TestSuite(map(calcDamage, testcasesCalcDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteCalcDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()