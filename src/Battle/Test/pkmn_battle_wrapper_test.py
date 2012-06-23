import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Status.faint import Faint

class reset(unittest.TestCase):
    """ Test cases of reset """
    
    def  setUp(self):
        """ Build the Pkmn """
        self.pkmn = BuildPokemonBattleWrapper()
        
    def statModsAreReset(self):
        """ Test that stats are actually reset """
        for key in self.pkmn.statMods:
            self.pkmn.statMods[key] = 2
        
        for key in self.pkmn.statMods:
            assert self.pkmn.statMods[key] == 2, "Stat should be changed"
            
        self.pkmn.reset()
        
        for key in self.pkmn.statMods:
            assert self.pkmn.statMods[key] == 0, "Stat should be zero"
        
    def flinchingIsReset(self):
        """ Test that flinching is reset """
        self.pkmn.flinching = True
        self.pkmn.reset()
        assert not self.pkmn.flinching, "Pkmn should not be flinching after reset"
        
    def lastActionIsReset(self):
        """ Test that lastAction is reset """
        self.pkmn.lastAction = 2
        self.pkmn.reset()
        assert self.pkmn.lastAction == None, "Pkmn should not have a lastAction after reset"
        
    def actionLockIsReset(self):
        """ Test that actionLock is reset """
        self.pkmn.actionLock = 2
        self.pkmn.reset()
        assert self.pkmn.actionLock == None, "Pkmn should not have a actionLock after reset"
        
    def dodgeIsReset(self):
        """ Test that dodge is reset """
        self.pkmn.dodge = 2
        self.pkmn.reset()
        assert self.pkmn.dodge == None, "Pkmn should not have a dodge after reset"
        
    def secondaryEffectsAreReset(self):
        """ Test that dodge is reset """
        self.pkmn.secondaryEffects = [2]
        self.pkmn.reset()
        assert self.pkmn.secondaryEffects == [], "Pkmn should not have any secondary effects after reset"

# Collect all test cases in this class
testcasesReset = ["statModsAreReset", "flinchingIsReset", "lastActionIsReset", "actionLockIsReset", "dodgeIsReset", "secondaryEffectsAreReset"]
suiteReset = unittest.TestSuite(map(reset, testcasesReset))

##########################################################

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

class betweenRounds(unittest.TestCase):
    """ Test cases of betweenRounds """
    
    def  setUp(self):
        """ Build the Pkmn """
        self.battlePkmn = BuildPokemonBattleWrapper()
        
    def resetFlinch(self):
        """ Test that flinch is reset between turns """
        self.battlePkmn.flinching = True
        
        self.battlePkmn.betweenRounds()
        
        assert self.battlePkmn.flinching == False, "Flinching should be reset to false"
        

# Collect all test cases in this class
testcasesBetweenRounds = ["resetFlinch"]
suiteBetweenRounds = unittest.TestSuite(map(betweenRounds, testcasesBetweenRounds))

##########################################################

class takeDamage(unittest.TestCase):
    """ Test cases of takeDamage """
    
    def  setUp(self):
        """ Build the Pkmn """
        self.pkmn = BuildPokemonBattleWrapper()
    
    def faints(self):
        """ Test that Faint Exception is thrown """
        messages = self.pkmn.takeDamage(self.pkmn.getCurrHP())
        assert messages == [self.pkmn.getHeader() + Faint.start], "The Pkmn should have fainted"
        
    def noFaint(self):
        """ Test that Faint Exception is not thrown if the pkmn doesn't faint """
        messages = self.pkmn.takeDamage(self.pkmn.getCurrHP()-1)
        assert messages == [], "Should receive any empty list when the Pkmn has not fainted"

# Collect all test cases in this class
testcasesTakeDamage= ["faints", "noFaint"]
suiteTakeDamage = unittest.TestSuite(map(takeDamage, testcasesTakeDamage))

##########################################################

# Collect all test cases in this file
suites = [suiteReset, suiteResetStatMods, suiteBetweenRounds, suiteTakeDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()