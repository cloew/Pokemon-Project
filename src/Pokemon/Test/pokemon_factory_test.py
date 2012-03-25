import unittest
from Test.test_helper import BuildPokemon

from Pokemon.pokemon_factory import PokemonFactory

class copy(unittest.TestCase):
    """ Test cases of copy """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.pkmn = BuildPokemon()
        self.copy = PokemonFactory.copy(self.pkmn)
        
    def name(self):
        """ Test that name is copied """
        assert self.copy.name == self.pkmn.name, "Should have copied name"
        
    def species(self):
        """ Test that species is copied """
        assert self.copy.species == self.pkmn.species, "Should have copied species"
        
    def level(self):
        """ Test that level is copied """
        assert self.copy.level == self.pkmn.level, "Should have copied level"
        
    def id(self):
        """ Test that id is copied """
        assert self.copy.id == self.pkmn.id, "Should have copied id"
        
    def ability(self):
        """ Test that ability is copied """
        assert self.copy.ability == self.pkmn.ability, "Should have copied ability"
        
    def battleDelegate(self):
        """ Test that battleDelegate is copied """
        assert self.copy.battleDelegate is not self.pkmn.battleDelegate, "Should have copied battleDelegate, but it should have a different address"

# Collect all test cases in this class
testcasesCopy = ["name", "species", "level", "id", "ability", "battleDelegate"]
suiteCopy = unittest.TestSuite(map(copy, testcasesCopy))

##########################################################

# Collect all test cases in this file
suites = [suiteCopy]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()