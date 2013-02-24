import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.swap_ability_delegate import SwapAbilityDelegate
from Pokemon.Abilities.ability import Ability

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn, Abilities and Effect for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.userAbility = Ability()
        self.targetAbility = Ability()
        
        self.user.setAbility(self.userAbility)
        self.target.setAbility(self.targetAbility)
        
        self.delegate = SwapAbilityDelegate()
        
    def swapped(self):
        """ Test that the abilities are swapped """
        self.delegate.applyEffect(self.user, self.target, None)
        
        assert self.user.getAbility() is self.targetAbility, "User should have target's ability"
        assert self.target.getAbility() is self.userAbility, "Target should have user's ability"
        
    def message(self):
        """ Test message is returned correctly """
        messages = self.delegate.applyEffect(self.user, self.target, None)
        
        assert messages == [SwapAbilityDelegate.message % (self.user.getHeader(), self.target.getHeader())], "Should have the Effect's message"

# Collect all test cases in this class
testcasesApplyEffect = ["swapped", "message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()