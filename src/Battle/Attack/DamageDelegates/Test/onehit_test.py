import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.attackfactory import AttackFactory
from Battle.Attack.DamageDelegates.onehit_delegate import OneHitDelegate

class damage(unittest.TestCase):
    """ Test cases of damage """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        attack = AttackFactory.getAttackAsNew("TACKLE")
        
        self.hp = 100
        self.target.setCurrHP(self.hp)
        
        self.delegate = OneHitDelegate(attack, 1)
        
    def oneHitKO(self):
        """ Test that the attack is a one-hit KO """
        self.target.setCurrHP(self.hp)
        self.target.pkmn.battleDelegate.types = ["NORMAL"]
        
        damage, messages = self.delegate.damage(self.user, self.target)
        assert damage == self.hp, "The damage should be the targets health"
        assert len(messages) == 1, "Should only get one message"
        assert messages[0] == OneHitDelegate.message, "Should get the One Hit KO message"
        
    def noDamage(self):
        """ Test that the attack does no damage when the effectiveness is 0 """
        self.target.pkmn.battleDelegate.types = ["GHOST"]
        
        damage, messages = self.delegate.damage(self.user, self.target)
        assert damage == 0, "The damage should be zero"

# Collect all test cases in this class
testcasesDamage = ["oneHitKO", "noDamage"]
suiteDamage = unittest.TestSuite(map(damage, testcasesDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()