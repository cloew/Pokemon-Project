from Pokemon.Abilities.sniper_ability import SniperAbility

import unittest

class giveCrit(unittest.TestCase):
    """ Test that giveCrit operates correctly """
    
    def setUp(self):
        """ Builds the ability for use in the tests """
        self.ability = SniperAbility("")
        
    def alwaysReturns3(self):
        """ Check gaurded stat is the only protected stat """
        newMod = self.ability.giveCrit(2)
        
        assert newMod == 3, "Mod should always be three."
        
testcasesGiveCrit = ["alwaysReturns3"]
suiteGiveCrit = unittest.TestSuite(map(giveCrit, testcasesGiveCrit))

##########################################################

 
suites = [suiteGiveCrit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()