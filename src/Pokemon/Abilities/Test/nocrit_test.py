from Pokemon.Abilities.nocrit_ability import NoCritAbility

import unittest

class onCrit(unittest.TestCase):
    """ Test that onCrit operates correctly """
    
    def setUp(self):
        """ Builds the ability for use in the tests """
        self.ability = NoCritAbility("")
        
    def alwaysReturns1(self):
        """ Check gaurded stat is the only protected stat """
        newMod = self.ability.onCrit(2)
        
        assert newMod == 1, "Mod should always be one."
        
testcasesOnCrit = ["alwaysReturns1"]
suiteOnCrit = unittest.TestSuite(map(onCrit, testcasesOnCrit))

##########################################################

 
suites = [suiteOnCrit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()