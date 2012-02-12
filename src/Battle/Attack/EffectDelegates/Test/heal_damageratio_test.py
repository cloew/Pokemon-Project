import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.heal_damageratio_delegate import HealByDamageRatioDelegate

class heal(unittest.TestCase):
    """ Test cases of heal """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.ratio = 2
        self.damage = 10
        self.delegate = HealByDamageRatioDelegate(self.ratio)
        
    def heal(self):
        """ Test that it heals by the ratio of the damage done """
        self.pkmn.setCurrHP(0)
        self.delegate.damage = self.damage
        self.delegate.heal(self.pkmn)
        
        hp = self.pkmn.getCurrHP()
        heal = self.damage/self.ratio
        assert hp == heal, "Should be healed by the damage over ratio"

# Collect all test cases in this class
testcasesHeal = ["heal"]
suiteHeal = unittest.TestSuite(map(heal, testcasesHeal))

##########################################################

# Collect all test cases in this file
suites = [suiteHeal]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()