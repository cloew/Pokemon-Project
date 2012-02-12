import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.reset_statmods_delegate  import ResetStatModsDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.delegate = ResetStatModsDelegate()
        
    def userReset(self):
        """ Test that the user's statmods are reset """
        for stat in self.user.statMods:
            self.user.statMods[stat] = 3
            
        self.delegate.applyEffect(self.user, self.target)
        
        for stat in self.user.statMods:
            assert self.user.statMods[stat] == 0, "Stat Mod should be reset to zero"
        
    def targetReset(self):
        """ Test that the target's statmods are reset """
        for stat in self.target.statMods:
            self.target.statMods[stat] = 3
            
        self.delegate.applyEffect(self.user, self.target)
        
        for stat in self.target.statMods:
            assert self.target.statMods[stat] == 0, "Stat Mod should be reset to zero"
        
    def message(self):
        """ Test that the proper message is returned """
        messages = self.delegate.applyEffect(self.user, self.target)
        
        assert messages == [ResetStatModsDelegate.message], "Should get the delegate's message"

# Collect all test cases in this class
testcasesApplyEffect = ["userReset", "targetReset", "message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()