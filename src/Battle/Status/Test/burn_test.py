from Battle.Status.burn import Burn

import unittest

class getStatMod(unittest.TestCase):
    """ Test that statMod returns the correct values for all stats """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Burn()
    
    def checkStatMods(self):
        """ Test that stat modifiers are correct for Burn
        .5 for ATK, 1 for the rest"""
        for key in self.status.statMods:
            if key == "ATK":
                assert self.status.getStatMod(key) == .5, "ATK should be .5"
            else:
                assert self.status.getStatMod(key) == 1, "All stats, except ATK, should be 1"
        
    
        
testcasesGetStatMod = ["checkStatMods"]
suiteGetStatMod = unittest.TestSuite(map(getStatMod, testcasesGetStatMod))

##########################################################

class immune(unittest.TestCase):
    """ Test that immune returns correctly """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Burn()
    
    def immune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["FIRE"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if FIRE"
        
        types = ["GROUND", "FIRE"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if FIRE regardless of other type"
            
    def notImmune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["ELECTRIC"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should not be immune if not FIRE"
        
testcasesImmune = ["immune", "notImmune"]
suiteImmune= unittest.TestSuite(map(immune, testcasesImmune))

##########################################################
 
suites = [suiteGetStatMod, suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()