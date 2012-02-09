import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.CritDelegates.crit_delegate import CritDelegate

class getCritChance(unittest.TestCase):
    """ Test cases of getCritChance """
    
    def  setUp(self):
        """ Build the CritDelegate and Pkmn for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.crit = CritDelegate(0)
        
    def checkMods(self):
        """ Test that mods affect the crit chance correctly """
        self.crit = CritDelegate(0)
        
        for mod in range(0, len(CritDelegate.critMods)):
            self.pkmn.statMods["CRT"] = mod
            chance = self.crit.getCritChance(self.pkmn)
            assert chance == CritDelegate.critMods[mod], "The Pkmn's crit mod should get the corresponding crit chance"
            
    def checkBase(self):
        """ Test that base affect the crit chance correctly """
        self.pkmn.statMods["CRT"] = 0
        
        for base in range(0, len(CritDelegate.critMods)):
            crit = CritDelegate(base)
            chance = crit.getCritChance(self.pkmn)
            assert chance == CritDelegate.critMods[base], "The Crit Delegate's base should get the corresponding crit chance"
            
    def checkBaseAndMod(self):
        """ Test that base and mod compound correctly """
        base = 2
        mod = 2
        
        self.crit = CritDelegate(base)
        self.pkmn.statMods["CRT"] = mod
        chance = self.crit.getCritChance(self.pkmn)
        assert chance == CritDelegate.critMods[base+mod], "The base and mod should compound to get the crit chance"
        

# Collect all test cases in this class
testcasesGetCritChance = ["checkMods", "checkBase", "checkBaseAndMod"]
suiteGetCritChance = unittest.TestSuite(map(getCritChance, testcasesGetCritChance))

##########################################################

class checkForCrit(unittest.TestCase):
    """ Test cases of checkForCrit """
    
    def  setUp(self):
        """ Build the CritDelegate and Pkmn for the test """
        self.crit = CritDelegate(0)
        
    def didCrit(self):
        """ Test that checkForCrit returns correctly when it did crit """
        critChance = 1
        rand = 0
        
        crit, message = self.crit.checkForCrit(critChance, rand)
        assert crit, "Should crit if critChance is greater than random"
        assert message == CritDelegate.critMessage, "Should return the crit message" 
        
            
    def didntCrit(self):
        """ Test that checkForCrit returns correctly when it did not crit """
        critChance = 0
        rand = 1
        
        crit, message = self.crit.checkForCrit(critChance, rand)
        assert not crit, "Should not crit if critChance is less than random"
        assert message == CritDelegate.critMessage, "Should return the crit message" 
        

# Collect all test cases in this class
testcasesCheckForCrit = ["didCrit", "didntCrit"]
suiteCheckForCrit = unittest.TestSuite(map(checkForCrit, testcasesCheckForCrit))

##########################################################

# Collect all test cases in this file
suites = [suiteGetCritChance, suiteCheckForCrit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()