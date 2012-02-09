import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.attackfactory import AttackFactory

class takeDamage(unittest.TestCase):
    """ Test cases of takeDamage """
    
    def  setUp(self):
        """ Build the Attack, Delegates and Pkmn for the test """
        self.attack = AttackFactory.getAttackAsNew("MEGA DRAIN")
        self.target = BuildPokemonBattleWrapper()
        self.damage = 20
        
    def setsDamage(self):
        """ Test that takeDamage sets the Damage on the Effect Delegate """
        self.attack.damageDelegate.takeDamage(self.damage, self.target)
        assert self.attack.effectDelegates[0].damage == self.damage, "Effect should have received the damage"

# Collect all test cases in this class
testcasesTakeDamage = ["setsDamage"]
suiteTakeDamage = unittest.TestSuite(map(takeDamage, testcasesTakeDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteTakeDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()