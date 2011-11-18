from Pokemon.Abilities.sniper_ability import SniperAbility

import unittest

class onCrit(unittest.TestCase):
    """ Test that onCrit operates correctly """
    
    def setUp(self):
        """ Builds the ability for use in the tests """
        self.ability = SniperAbility("")
        
    def alwaysReturns3(self):
        """ Check gaurded stat is the only protected stat """
        newMod = self.ability.onCrit(2)
        
        assert newMod == 3, "Mod should always be three."
        
testcasesOnCrit = ["alwaysReturns3"]
suiteOnCrit = unittest.TestSuite(map(onCrit, testcasesOnCrit))

##########################################################

 
suites = [suiteOnCrit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()