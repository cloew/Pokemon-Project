import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

class doDamage(unittest.TestCase):
    """ Test cases of doDamage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.delegate = NullDamageDelegate()
        
    def none(self):
        """ Test that doDamage returns None """
        ret = self.delegate.doDamage(self.user, self.target)
        assert ret is None, "Should return None"

# Collect all test cases in this class
testcasesDoDamage = ["none"]
suiteDoDamage = unittest.TestSuite(map(doDamage, testcasesDoDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteDoDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()