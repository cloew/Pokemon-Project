import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Pokemon.Abilities.skip_turn_ability import SkipTurnAbility

class stopAttack(unittest.TestCase):
    """ Test cases of stopAttack """
    
    def  setUp(self):
        """ Build the Ability and Pkmn for the test """
        self.ability = SkipTurnAbility(None)
        self.pkmn = BuildPokemonBattleWrapper()
        
    def stop(self):
        """ Test that the ability returns correctly when it should stop """
        self.ability.stop = 0
        stop, messages = self.ability.stopAttack(self.pkmn)
        
        assert stop, "Should stop"
        assert messages == [self.pkmn.getHeader() + SkipTurnAbility.message], "Should receive message that the Pkmn is loafing"
        
    def noStop(self):
        """ Test that the ability returns correctly when it should not stop """
        self.ability.stop = 1
        stop, messages = self.ability.stopAttack(self.pkmn)
        
        assert not stop, "Should not stop"
        assert messages == [], "Should not receive any messages"

# Collect all test cases in this class
testcasesStopAttack = ["stop", "noStop"]
suiteStopAttack = unittest.TestSuite(map(stopAttack, testcasesStopAttack))

##########################################################

class toggleStop(unittest.TestCase):
    """ Test cases of toggleStop """
    
    def  setUp(self):
        """ Build the Ability and Pkmn for the test """
        self.ability = SkipTurnAbility(None)
        self.pkmn = BuildPokemonBattleWrapper()
        
    def stop(self):
        """ Test that stop is toggled to True """
        self.ability.stop = 0
        self.ability.toggleStop()
        
        assert self.ability.stop, "Should stop"
        
    def noStop(self):
        """ Test that stop is toggled False """
        self.ability.stop = 1
        self.ability.toggleStop()
        
        assert not self.ability.stop, "Should not stop"

# Collect all test cases in this class
testcasesToggleStop = ["stop", "noStop"]
suiteToggleStop = unittest.TestSuite(map(toggleStop, testcasesToggleStop))

##########################################################

# Collect all test cases in this file
suites = [suiteStopAttack, suiteToggleStop]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()