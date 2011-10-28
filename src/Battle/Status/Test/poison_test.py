from Battle.Status.poison import Poison

import unittest

class immune(unittest.TestCase):
    """ Test that immune returns correctly """
    
    def setUp(self):
        """ Builds the Poison status"""
        self.status = Poison()
    
    def immune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["STEEL"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if STEEL"
        
        types = ["POISON", "FIRE"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if POSION"
            
    def notImmune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["ELECTRIC"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should not be immune if not POISON or STEEL"
        
testcasesImmune = ["immune", "notImmune"]
suiteImmune = unittest.TestSuite(map(immune, testcasesImmune))

##########################################################
 
suites = [suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()