from Pokemon.Abilities.nocrit_ability import NoCritAbility

import unittest

class takeCrit(unittest.TestCase):
    """ Test that takeCrit operates correctly """
    
    def setUp(self):
        """ Builds the ability for use in the tests """
        self.ability = NoCritAbility("")
        
    def alwaysReturns1(self):
        """ Check gaurded stat is the only protected stat """
        newMod, messages = self.ability.takeCrit(2, None, None)
        
        assert newMod == 1, "Mod should always be one."
        assert len(messages) == 0, "Should have no messages"
        
testcasesTakeCrit = ["alwaysReturns1"]
suiteTakeCrit = unittest.TestSuite(map(takeCrit, testcasesTakeCrit))

##########################################################

 
suites = [suiteTakeCrit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()