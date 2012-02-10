import unittest
from Test.test_helper import *

from Battle.Attack.DamageDelegates.level_delegate import LevelDelegate

class calcDamage(unittest.TestCase):
    """ Test cases of calcDamage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.level = 30
        self.user.pkmn.level = self.level
        
        self.delegate = LevelDelegate(None, 1)
        
    def level(self):
        """ Test that the damage is the Pkmns Level"""
        self.user.statMods["ATK"] = 0
        damage =  self.delegate.calcDamage(self.user, self.target)
        assert damage == self.level, "Damage should be the users level"
        
    def levelWithStatMod(self):
        """ Test that the damage returned is the level even with a stat mod """
        self.user.statMods["ATK"] = 3
        damage =  self.delegate.calcDamage(self.user, self.target)
        assert damage == self.level, "Damage should be the users level"

# Collect all test cases in this class
testcasesCalcDamage = ["level", "levelWithStatMod"]
suiteCalcDamage = unittest.TestSuite(map(calcDamage, testcasesCalcDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteCalcDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()