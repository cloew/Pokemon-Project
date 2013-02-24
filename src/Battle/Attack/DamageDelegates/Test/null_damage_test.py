import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.battle_environment import BattleEnvironment
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

class doDamage(unittest.TestCase):
    """ Test cases of doDamage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.environment = BattleEnvironment()
        
        self.delegate = NullDamageDelegate()
        
    def noMessages(self):
        """ Test that doDamage returns no messages """
        messages = self.delegate.doDamage(self.user, self.target, self.environment)
        assert messages == [], "Should return no messages"

# Collect all test cases in this class
testcasesDoDamage = ["noMessages"]
suiteDoDamage = unittest.TestSuite(map(doDamage, testcasesDoDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteDoDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()