import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Pokemon.Abilities.statmodonstatus_ability import StatModOnStatusAbility

from Battle.Status.status import Status
from Battle.Status.paralysis import Paralysis

class onStatus(unittest.TestCase):
    """ Test that onStatus operates correctly"""
    
    def setUp(self):
        """ Builds the ability and Pkmn for use in the tests """
        self.battlePkmn = BuildPokemonBattleWrapper()
        self.status = Paralysis()
        self.status2 = Status()
        self.stat = "ATK"
        self.mod = 1.5
        
        self.ability = StatModOnStatusAbility("", self.stat, self.mod)
        
    def statChange(self):
        """ Check that the stat is actually changed """
        messages = self.ability.onStatus(self.battlePkmn, self.status)
        
        assert self.status.statMods[self.stat] == self.mod, "Stat Mod should be the modified stat."
        assert len(messages) == 1, "Messages should have one element"
        
testcasesOnStatus = ["statChange"]
suiteOnStatus = unittest.TestSuite(map(onStatus, testcasesOnStatus))

##########################################################

 
suites = [suiteOnStatus]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()