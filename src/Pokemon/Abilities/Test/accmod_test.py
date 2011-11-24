from Pokemon.Abilities.accmod_ability import AccModAbility

import unittest

class onAccuracy(unittest.TestCase):
    """ Test that onAccuracy returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.mod = 1.3
        self.ability = AccModAbility("", self.mod)
        self.accuracy = 90
        
    def properReturnValues(self):
        """ Check that onStatMod returns the proper default values """
        accuracy = self.ability.onAccuracy(self.accuracy)
        assert accuracy == self.accuracy*self.mod, "Accuracy should be altered by the mod."
        
testcasesOnAccuracy = ["properReturnValues"]
suiteOnAccuracy = unittest.TestSuite(map(onAccuracy, testcasesOnAccuracy))

##########################################################

 
suites = [suiteOnAccuracy]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()