import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.piercedodge_2Xdelegate import PierceDodge2XDelegate

class coreDamage(unittest.TestCase):
    """ Test cases of coreDamage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.dodge = "DIG"        
        self.delegate = PierceDodge2XDelegate(None, 20, 1, self.dodge)
        self.standard = DamageDelegate(None, 20, 1)
        
    def pierce(self):
        """ Test that the damage is doubled on pierce """
        self.target.dodge = self.dodge
        standard = self.standard.coreDamage(self.user, self.target)
        damage = self.delegate.coreDamage(self.user, self.target)
        
        assert damage == standard*2 , "The damage should be double on pierce"
        
    def noPierce(self):
        """ Test that the damage is standard when there is no pierce """
        self.target.dodge = None
        standard = self.standard.coreDamage(self.user, self.target)
        damage = self.delegate.coreDamage(self.user, self.target)
        
        assert damage == standard , "The damage should be standard on no pierce"

# Collect all test cases in this class
testcasesCoreDamage = ["pierce", "noPierce"]
suiteCoreDamage = unittest.TestSuite(map(coreDamage, testcasesCoreDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteCoreDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()