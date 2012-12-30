import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.swap_stat_delegate import SwapStatDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Effect and Pkmn for the test """
        self.stat1 = "ATK"
        self.stat2 = "DEF"
        
        self.val1 = 50
        self.val2 = 20
        
        self.user = BuildPokemonBattleWrapper()
        self.delegate = SwapStatDelegate(self.stat1, self.stat2)
        
    def swapped(self):
        """ Test that the stats are swapped """
        self.user.setStat(self.stat1, self.val1)
        self.user.setStat(self.stat2, self.val2)
        self.delegate.applyEffect(self.user, None, None)
        
        assert self.user.getStat(self.stat1) == self.val2, "Stat 1 should get Stat 2's value"
        assert self.user.getStat(self.stat2) == self.val1, "Stat 2 should get Stat 1's value"
        
    def message(self):
        """ Test that the message is returned correctly """
        messages = self.delegate.applyEffect(self.user, None, None)
        
        message = SwapStatDelegate.message % (self.user.getHeader(), self.stat1, self.stat2)
        assert messages == [message], "Message should say the user had its two stats swapped"

# Collect all test cases in this class
testcasesApplyEffect = ["swapped"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()