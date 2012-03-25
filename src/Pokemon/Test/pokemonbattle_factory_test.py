import unittest
from Test.test_helper import *

class copy(unittest.TestCase):
    """ Test cases of copy """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.pkmn = BuildPokemon()
        self.delegate = self.pkmn.battleDelegate
        self.copyPkmn = PokemonFactory.copy(self.pkmn)
        self.copy = self.copyPkmn.battleDelegate
        
    def parent(self):
        """ Test that parent is copied """
        assert self.copy.parent is not self.delegate.parent, "Should have copied parent, but it should have a different address"
        assert self.copy.parent is self.copyPkmn, "Should have copied parent, but it should have a different address"
        
    def currHP(self):
        """ Test that currHP is copied """
        assert self.copy.currHP == self.delegate.currHP, "Should have copied currHP"
        
    def attacks(self):
        """ Test that attacks is copied """
        assert self.copy.attacks == self.delegate.attacks, "Should have copied attacks"
        
    def status(self):
        """ Test that status is copied """
        assert self.copy.status == self.delegate.status, "Should have copied status"
        
    def types(self):
        """ Test that types is copied """
        assert self.copy.types == self.delegate.types, "Should have copied types"
        self.copy.types.append(1)
        assert self.copy.types is not self.delegate.types, "Should have separate types"
        
    def stats(self):
        """ Test that stats is copied """
        assert self.copy.stats is not self.delegate.stats, "Should have copied stats, but it should have a different address"
        self.copy.stats['1'] = 1
        assert self.copy.stats is not self.delegate.stats, "Should have separate stats"

# Collect all test cases in this class
testcasesCopy = ["parent", "currHP", "attacks", "status", "types", "stats"]
suiteCopy = unittest.TestSuite(map(copy, testcasesCopy))

##########################################################

# Collect all test cases in this file
suites = [suiteCopy]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()