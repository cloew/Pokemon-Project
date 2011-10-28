from Battle.Status.status import Status

import unittest

class getStatMod(unittest.TestCase):
    """ Test that statMod returns the correct values for all stats """
    
    def setUp(self):
        """ Builds the Status object"""
        self.status = Status()
    
    def checkStatMods(self):
        """ Test that stat modifiers are correct for generic status """
        for key in self.status.statMods:
            assert self.status.getStatMod(key) == 1, "All stats should be 1"
    
        
testcasesGetStatMod = ["checkStatMods"]
suiteGetStatMod = unittest.TestSuite(map(getStatMod, testcasesGetStatMod))

##########################################################

class immune(unittest.TestCase):
    """ Test that immune returns correctly """
    def setUp(self):
        """ Builds the status"""
        self.status = Status()
            
    def notImmune(self):
        """ Test if it can correctly identify when the target is not immune """
        types = ["ELECTRIC"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should never be immune."
        
testcasesImmune = ["notImmune"]
suiteImmune = unittest.TestSuite(map(immune, testcasesImmune))

##########################################################
 
suites = [suiteGetStatMod, suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()