from Pokemon.Abilities.ability import Ability

import unittest

class onStatMod(unittest.TestCase):
    """ Test that onStatMod returns the correct default values """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        self.degree = 1
        
    def properReturnValues(self):
        """ Check that onStatMod returns the proper default values """
        degree, messages = self.ability.onStatMod(None, None, self.degree)
        
        assert degree == self.degree, "Degree should be unmodified."
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesOnStatMod = ["properReturnValues"]
suiteOnStatMod = unittest.TestSuite(map(onStatMod, testcasesOnStatMod))

##########################################################

class onStatus(unittest.TestCase):
    """ Test that onStatus returns the correct default values """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        
    def properReturnValues(self):
        """ Check that onStatus returns the proper default values """
        messages = self.ability.onStatus(None, None)
        
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesOnStatus = ["properReturnValues"]
suiteOnStatus = unittest.TestSuite(map(onStatus, testcasesOnStatus))

##########################################################

 
suites = [suiteOnStatMod, suiteOnStatus]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()