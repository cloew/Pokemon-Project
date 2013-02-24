import unittest

from Pokemon.Abilities.confusion_immunity_ability import ConfusionImmunityAbility
from Test.test_helper import BuildPokemonBattleWrapper

class canBeConfused(unittest.TestCase):
    """ Test that canBeConfused returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.name = "Some Name"
        self.pkmn = BuildPokemonBattleWrapper()
        self.ability = ConfusionImmunityAbility(self.name)
        
    def properReturnValues(self):
        """ Check that canBeConfused returns the proper default values """
        messages = []
        assert not self.ability.canBeConfused(self.pkmn, messages), "Should not be able to be Confused"
        assert len(messages) == 1, "Should only have one message"
        assert messages[0] == "{0}'s {1} prevented confusion.".format(self.pkmn.getName(), self.name), "Message should have the Pkmn's name and ability's name"
        
testcasesCanBeConfused = ["properReturnValues"]
suiteCanBeConfused = unittest.TestSuite(map(canBeConfused, testcasesCanBeConfused))

##########################################################

suites = [suiteCanBeConfused]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()