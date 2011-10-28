import unittest

from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer

class resetStatMods(unittest.TestCase):
    """ Test cases of resetStatMods """
    
    def  setUp(self):
        """ Build the Trainer and side for the Battle"""
        trainer = Trainer()
        trainer.beltPokemon = []
        self.side = BattleSide(trainer)
        
    def statModsAreReset(self):
        """ Test that stats are actually reset """
        for key in self.side.statMods:
            self.side.statMods[key] = 2
        
        for key in self.side.statMods:
            assert self.side.statMods[key] == 2, "Stat should be changed"
            
        self.side.resetStatMods()
        
        for key in self.side.statMods:
            assert self.side.statMods[key] == 0, "Stat should be zero"

# Collect all test cases in this class
testcasesResetStatMods = ["statModsAreReset"]
suiteResetStatMods = unittest.TestSuite(map(resetStatMods, testcasesResetStatMods))

##########################################################

class betweenTurns(unittest.TestCase):
    """ Test cases of betweenTurns """
    
    def  setUp(self):
        """ Build the Trainer and side for the Battle"""
        trainer = Trainer()
        trainer.beltPokemon = []
        self.side = BattleSide(trainer)
        
    def resetFlinch(self):
        """ Test that flinch is reset between turns """
        self.side.flinching = True
        
        self.side.betweenTurns()
        
        assert self.side.flinching == False, "Flinching should be reset to false"
        

# Collect all test cases in this class
testcasesBetweenTurns= ["resetFlinch"]
suiteBetweenTurns = unittest.TestSuite(map(betweenTurns, testcasesBetweenTurns))

##########################################################
# Collect all test cases in this file
suites = [suiteResetStatMods, suiteBetweenTurns]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()