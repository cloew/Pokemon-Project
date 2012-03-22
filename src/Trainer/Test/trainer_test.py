import unittest
from Test.test_helper import BuildPokemon, BuildPokemonBattleWrapper, BuildAttackAction, BuildActionLock

from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

class getAction(unittest.TestCase):
    """ Test cases of getAction """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = Trainer()
        self.user = BuildPokemonBattleWrapper(trainer = self.trainer)
        
        self.attackAction = BuildAttackAction()
        self.actionLock = BuildActionLock(attackAction = self.attackAction)
        
    def hasLock(self):
        """ Check that the action is the Pkmn's Lock """
        self.user.actionLock = self.actionLock
        
        action = self.trainer.getAction(self.user, [None])
        assert action is self.attackAction, "Should be the lock's action"
        
    def noLock(self):
        """ Check the action is from Pick Action """
        self.user.actionLock = None
        
        action = self.trainer.getAction(self.user, [None])
        picked = self.trainer.pickAction(self.user, [None])
        assert action.user == picked.user, "Should have the same user"
        assert action.target == picked.target, "Should have the same target"
        assert action.attack == picked.attack, "Should have the same attack"

# Collect all test cases in this class
testcasesGetAction = ["hasLock",  "noLock"]
suiteGetAction  = unittest.TestSuite(map(getAction, testcasesGetAction))

##########################################################

class getPokemon(unittest.TestCase):
    """ Test cases of getPokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = Trainer()
        self.pkmnWithHealth = BuildPokemon(pkmn = "BULBASAUR")
        self.pkmnWithoutHealth = BuildPokemon(pkmn = "CHARMANDER")
        self.pkmnWithoutHealth.battleDelegate.currHP = 0
        
    def firstIsValid(self):
        """ Test if it actually correctly aquires the first Pkmn """
        self.trainer.beltPokemon = [self.pkmnWithHealth, self.pkmnWithoutHealth]
        
        assert self.trainer.getPokemon(0) is self.pkmnWithHealth, "Should get the first Pkmn"

        
    def firstIsFainted(self):
        """ Test if accurately skips a Pokemon with no HP """
        self.trainer.beltPokemon = [self.pkmnWithoutHealth, self.pkmnWithHealth]
        
        assert self.trainer.getPokemon(0) is self.pkmnWithHealth, "Should skip Pkmn w/out health"

# Collect all test cases in this class
testcasesGetPokemon = ["firstIsValid", "firstIsFainted"]
suiteGetPokemon  = unittest.TestSuite(map(getPokemon, testcasesGetPokemon))

##########################################################

class hasMorePokemon(unittest.TestCase):
    """ Test cases of hasMorePokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = Trainer()
        self.pkmnWithHealth = BuildPokemon(pkmn = "BULBASAUR")
        self.pkmnWithoutHealth = BuildPokemon(pkmn = "CHARMANDER")
        self.pkmnWithoutHealth.battleDelegate.currHP = 0
        
    def hasMorePokemon(self):
        """ Test the trainer actually has more Pokemon """
        self.trainer.beltPokemon = [self.pkmnWithHealth]
        
        assert self.trainer.hasMorePokemon([]) is True, "Should have more Pokemon"

        
    def noMorePokemon(self):
        """ Test the trainer has no more Pokemon """
        self.trainer.beltPokemon = [self.pkmnWithoutHealth]
        
        assert self.trainer.hasMorePokemon([]) is False, "Should not have more Pokemon"

# Collect all test cases in this class
testcasesHasMorePokemon = ["hasMorePokemon", "noMorePokemon"]
suiteHasMorePokemon  = unittest.TestSuite(map(hasMorePokemon, testcasesHasMorePokemon))

##########################################################
# Collect all test cases in this file
suites = [suiteGetAction, suiteGetPokemon, suiteHasMorePokemon]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()