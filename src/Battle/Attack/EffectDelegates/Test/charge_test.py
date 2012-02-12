from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.charge_delegate import ChargeDelegate

import unittest

class isCharging(unittest.TestCase):
    """ Test that isCharging returns the correct values """
    def setUp(self):
        """ Grabs the message dictionary from StatModDelegate """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = ChargeDelegate(2, 0, "")
        
    def isCharging(self):
        """ Tests if isCharging returns correctly when it is charging """
        self.delegate.turnOn = 1
        assert self.delegate.isCharging(self.pkmn), "Should be charging"
        
    def isNotCharging(self):
        """ Tests if isCharging returns correctly when it is not charging """
        self.delegate.turnOn = 0
        assert not self.delegate.isCharging(self.pkmn), "Should not be charging"
        
testcasesIsCharging = ["isCharging", "isNotCharging"]
suiteIsCharging = unittest.TestSuite(map(isCharging, testcasesIsCharging))

##########################################################
 
suites = [suiteIsCharging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()