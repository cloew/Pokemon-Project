from Battle.Status.paralysis import Paralysis

import unittest

class getStatMod(unittest.TestCase):
    """ Test that statMod returns the correct values for all stats """
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Paralysis()
    
    def checkStatMods(self):
        """ Test that stat modifiers are correct for Paralysis
        .75 for SPD, 1 for the rest"""
        for key in self.status.statMods:
            if key == "SPD":
                assert self.status.getStatMod(key) == .25, "SPD should be .25"
            else:
                assert self.status.getStatMod(key) == 1, "All stats, except SPD, should be 1"
        
    
        
testcasesGetStatMod = ["checkStatMods"]
suiteGetStatMod = unittest.TestSuite(map(getStatMod, testcasesGetStatMod))

##########################################################

class paralyzed(unittest.TestCase):
    """ Test that paralyzed returns correct for the right values """
    
    def paralyzed(self):
        """ Test if values for paralyzed return correctly """
        for i in range(25):
            assert Paralysis.paralyzed(i), "Should be paralyzed on 0-24"
            
    def notParalyzed(self):
        """ Test if values for paralyzed return correctly """
        for i in range(25, 100):
            assert not Paralysis.paralyzed(i), "Should be paralyzed on 0-24"
        
    
        
testcasesParalyzed = ["paralyzed", "notParalyzed"]
suiteParalyzed= unittest.TestSuite(map(paralyzed, testcasesParalyzed))

##########################################################

class immune(unittest.TestCase):
    """ Test that immune returns correctly """
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Paralysis()
    
    def immune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["GROUND"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if GROUND and ELECTRIC combo"
        
        types = ["GROUND", "ELECTRIC"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if GROUND and ELECTRIC combo regardless of other type"
        
        types = ["ELECTRIC", "GROUND"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if GROUND and ELECTRIC combo regardless of other type"
            
    def notImmune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["FIRE"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should not be immune if not GROUND and ELECTRIC combo"
        
        types = ["FIRE", "ELECTRIC"]
        other = "GROUND"
        assert not self.status.immune(types, other), "Should not be immune if not GROUND and ELECTRIC combo in the right order"
        
        types = ["GROUND", "ELECTRIC"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should not be immune if only GROUND"
        
        types = ["ELECTRIC"]
        other = "ELECTRIC"
        assert not self.status.immune(types, other), "Should not be immune if only ELECTRIC"
        
testcasesImmune = ["immune", "notImmune"]
suiteImmune= unittest.TestSuite(map(immune, testcasesImmune))

##########################################################
 
suites = [suiteGetStatMod, suiteParalyzed, suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()