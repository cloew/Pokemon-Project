import unittest

from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

class getPokemon(unittest.TestCase):
    """ Test cases of getPokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = Trainer()
        self.pokeWithHealth = Pokemon("BULBASAUR")
        self.pokeWithoutHealth = Pokemon("CHARMANDER")
        self.pokeWithoutHealth.battleDelegate.currHP = 0
        
    def firstIsValid(self):
        """ Test if it actually correctly aquires the first Pkmn """
        self.trainer.beltPokemon = [self.pokeWithHealth, self.pokeWithoutHealth]
        
        assert self.trainer.getPokemon(0) is self.pokeWithHealth, "Should get the first Pkmn"

        
    def firstIsFainted(self):
        """ Test if accurately skips a Pokemon with no HP """
        self.trainer.beltPokemon = [self.pokeWithoutHealth, self.pokeWithHealth]
        
        assert self.trainer.getPokemon(0) is self.pokeWithHealth, "Should skip Pkmn w/out health"

# Collect all test cases in this class
testcasesGetPokemon = ["firstIsValid", "firstIsFainted"]
suiteGetPokemon  = unittest.TestSuite(map(getPokemon, testcasesGetPokemon))

##########################################################

class hasMorePokemon(unittest.TestCase):
    """ Test cases of hasMorePokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = Trainer()
        self.pokeWithHealth = Pokemon("BULBASAUR")
        self.pokeWithoutHealth = Pokemon("CHARMANDER")
        self.pokeWithoutHealth.battleDelegate.currHP = 0
        
    def hasMorePokemon(self):
        """ Test the trainer actually has more Pokemon """
        self.trainer.beltPokemon = [self.pokeWithHealth]
        
        assert self.trainer.hasMorePokemon() is True, "Should have more Pokemon"

        
    def noMorePokemon(self):
        """ Test the trainer has no more Pokemon """
        self.trainer.beltPokemon = [self.pokeWithoutHealth]
        
        assert self.trainer.hasMorePokemon() is False, "Should not have more Pokemon"

# Collect all test cases in this class
testcasesHasMorePokemon = ["hasMorePokemon", "noMorePokemon"]
suiteHasMorePokemon  = unittest.TestSuite(map(hasMorePokemon, testcasesHasMorePokemon))

##########################################################
# Collect all test cases in this file
suites = [suiteGetPokemon, suiteHasMorePokemon]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()