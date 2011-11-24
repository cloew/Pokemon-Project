from Pokemon.Abilities.ability import Ability

import unittest

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability()
        
    def properReturnValues(self):
        """ Check that afterTurn returns the proper default values """
        messages = self.ability.afterTurn(None, None)
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesAfterTurn = ["properReturnValues"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class canUseEffects(unittest.TestCase):
    """ Test that canUseEffects returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability()
        
    def properReturnValues(self):
        """ Check that afterTurn returns the proper default values """
        can = self.ability.canUseEffects()
        assert can, "Should be able to use Effects"
        
testcasesCanUseEffects = ["properReturnValues"]
suiteCanUseEffects = unittest.TestSuite(map(canUseEffects, testcasesCanUseEffects))

##########################################################

class giveCrit(unittest.TestCase):
    """ Test that giveCrit returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        self.mod = 2
        
    def properReturnValues(self):
        """ Check that giveCrit returns the proper default values """
        mod = self.ability.giveCrit(self.mod)
        
        assert mod == self.mod, "Mod should not be altered."
        
testcasesGiveCrit = ["properReturnValues"]
suiteGiveCrit = unittest.TestSuite(map(giveCrit, testcasesGiveCrit))

##########################################################

class takeCrit(unittest.TestCase):
    """ Test that takeCrit returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        self.mod = 2
        
    def properReturnValues(self):
        """ Check that takeCrit returns the proper default values """
        mod, messages = self.ability.takeCrit(self.mod, None, None)
        
        assert mod == self.mod, "Mod should not be altered."
        assert len(messages) == 0, "Should have no messages returned."
        
testcasesTakeCrit = ["properReturnValues"]
suiteTakeCrit = unittest.TestSuite(map(takeCrit, testcasesTakeCrit))

##########################################################

class onAccuracy(unittest.TestCase):
    """ Test that onAccuracy returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability()
        self.accuracy = 90
        
    def properReturnValues(self):
        """ Check that onAccuracy returns the proper default values """
        accuracy = self.ability.onAccuracy(self.accuracy)
        assert accuracy == self.accuracy, "Accuracy should be unaltered."
        
testcasesOnAccuracy = ["properReturnValues"]
suiteOnAccuracy = unittest.TestSuite(map(onAccuracy, testcasesOnAccuracy))

##########################################################

class onStab(unittest.TestCase):
    """ Test that onStab returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        
    def properReturnValues(self):
        """ Check that onStatMod returns the proper default values """
        mod = self.ability.onStab()
        
        assert mod == self.ability.stabMod, "Stab Mod should be default."
        
testcasesOnStab = ["properReturnValues"]
suiteOnStab = unittest.TestSuite(map(onStab, testcasesOnStab))

##########################################################

class onStatMod(unittest.TestCase):
    """ Test that onStatMod returns the correct default values """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability()
        self.degree = 1
        
    def properReturnValues(self):
        """ Check that onStatMod returns the proper default values """
        degree, messages = self.ability.onStatMod(None, None, self.degree, None)
        
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

 
suites = [suiteAfterTurn, suiteCanUseEffects, suiteGiveCrit, suiteTakeCrit,\
             suiteOnAccuracy, suiteOnStab, suiteOnStatMod, suiteOnStatus]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()