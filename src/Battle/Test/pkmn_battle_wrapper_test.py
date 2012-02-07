import unittest
from Test.test_helper import BuildPokemonBattleWrapper

class resetStatMods(unittest.TestCase):
    """ Test cases of resetStatMods """
    
    def  setUp(self):
        """ Build the Pkmn """
        self.battlePkmn = BuildPokemonBattleWrapper()
        
    def statModsAreReset(self):
        """ Test that stats are actually reset """
        for key in self.battlePkmn.statMods:
            self.battlePkmn.statMods[key] = 2
        
        for key in self.battlePkmn.statMods:
            assert self.battlePkmn.statMods[key] == 2, "Stat should be changed"
            
        self.battlePkmn.resetStatMods()
        
        for key in self.battlePkmn.statMods:
            assert self.battlePkmn.statMods[key] == 0, "Stat should be zero"

# Collect all test cases in this class
testcasesResetStatMods = ["statModsAreReset"]
suiteResetStatMods = unittest.TestSuite(map(resetStatMods, testcasesResetStatMods))

##########################################################

class betweenTurns(unittest.TestCase):
    """ Test cases of betweenTurns """
    
    def  setUp(self):
        """ Build the Pkmn """
        self.battlePkmn = BuildPokemonBattleWrapper()
        
    def resetFlinch(self):
        """ Test that flinch is reset between turns """
        self.battlePkmn.flinching = True
        
        self.battlePkmn.betweenTurns()
        
        assert self.battlePkmn.flinching == False, "Flinching should be reset to false"
        

# Collect all test cases in this class
testcasesBetweenTurns= ["resetFlinch"]
suiteBetweenTurns = unittest.TestSuite(map(betweenTurns, testcasesBetweenTurns))

##########################################################

# Collect all test cases in this file
suites = [suiteResetStatMods, suiteBetweenTurns]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()