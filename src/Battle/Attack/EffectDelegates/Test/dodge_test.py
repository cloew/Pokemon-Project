import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.battle_environment import BattleEnvironment
from Battle.Attack.EffectDelegates.dodge_delegate import DodgeDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.delegate = DodgeDelegate("DIG", "")
        
    def dodgeRemoved(self):
        """ Test that the dodge is removed when the attack's effect is applied """
        self.delegate.applyEffect(self.user, self.target, None)
        assert self.user.dodge == None, "User should no longer be dodging"

# Collect all test cases in this class
testcasesApplyEffect = ["dodgeRemoved"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class isCharging(unittest.TestCase):
    """ Test cases of isCharging """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.environment = BattleEnvironment()
        self.dodgeType = "DIG"
        self.delegate = DodgeDelegate(self.dodgeType, "")
        
    def dodging(self):
        """ Test that the dodge is set to the delegate's dodge type """
        assert self.user.dodge is None, "User should not be dodging"
        self.delegate.isCharging(self.user, self.environment)
        assert self.user.dodge == self.dodgeType, "User should get the delegate's dodge type"

# Collect all test cases in this class
testcasesIsCharging = ["dodging"]
suiteIsCharging = unittest.TestSuite(map(isCharging, testcasesIsCharging))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect, suiteIsCharging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()