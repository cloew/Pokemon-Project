import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.swapstatmods_delegate import SwapStatModsDelegate

class applyEffect(unittest.TestCase):
    """ Test that isCharging returns the correct values """
    def setUp(self):
        """ Grabs the message dictionary from StatModDelegate """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.delegate = SwapStatModsDelegate()
        
        self.statMods1 = {"ATK":1, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":1}
        self.user.statMods = self.statMods1
                                
        self.statMods2 = {"ATK":0, "DEF":0, "SPD":1, "SATK":1, "SDEF":1, 
                                "ACC":0, "EVAS":0, "CRT":0}
        self.target.statMods = self.statMods2
        
    def statModsSwitched(self):
        """ Tests if ithe stat mods are swapped """
        self.delegate.applyEffect(self.user, self.target)
        assert self.user.statMods == self.statMods2, "Pkmn 1 should have stats from Pkmn 2"
        assert self.target.statMods == self.statMods1, "Pkmn 2 should have stats from Pkmn 1"
        
    def message(self):
        """ Test the message returned is correct """
        messages = self.delegate.applyEffect(self.user, self.target)
        message = self.user.getHeader() + SwapStatModsDelegate.message
        assert len(messages) == 1, "Should get 1 message"
        assert messages[0] == message, "Should be Pkmn's header and the Delegate's message"
        
testcasesApplyEffect= ["statModsSwitched", "message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################
 
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()