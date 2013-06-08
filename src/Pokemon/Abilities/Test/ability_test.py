import unittest

from Pokemon.Abilities.ability import Ability
from Test.test_helper import BuildPokemonBattleWrapper

class stopAttack(unittest.TestCase):
    """ Test that stopAttack returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that stopAttack returns the proper default values """
        stop, messages = self.ability.stopAttack(None)
        assert not stop, "Should not stop"
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesStopAttack = ["properReturnValues"]
suiteStopAttack = unittest.TestSuite(map(stopAttack, testcasesStopAttack))

##########################################################

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that afterTurn returns the proper default values """
        messages = self.ability.afterTurn(None)
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesAfterTurn = ["properReturnValues"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class canUseEffects(unittest.TestCase):
    """ Test that canUseEffects returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that afterTurn returns the proper default values """
        can = self.ability.canUseEffects()
        assert can, "Should be able to use Effects"
        
testcasesCanUseEffects = ["properReturnValues"]
suiteCanUseEffects = unittest.TestSuite(map(canUseEffects, testcasesCanUseEffects))

##########################################################

class canBeConfused(unittest.TestCase):
    """ Test that canBeConfused returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.pkmn = BuildPokemonBattleWrapper()
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that canBeConfused returns the proper default values """
        assert self.ability.canBeConfused(None, []), "Should be able to be Confused"
        
    def properReturnValues_NoMessagesObject(self):
        """ Check that canBeConfused returns the proper default values """
        assert self.ability.canBeConfused(None, None), "Should be able to be Confused"
        
testcasesCanBeConfused = ["properReturnValues", "properReturnValues_NoMessagesObject"]
suiteCanBeConfused = unittest.TestSuite(map(canBeConfused, testcasesCanBeConfused))

##########################################################

class giveCrit(unittest.TestCase):
    """ Test that giveCrit returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability(None)
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
        self.ability = Ability(None)
        self.mod = 2
        
    def properReturnValues(self):
        """ Check that takeCrit returns the proper default values """
        mod, messages = self.ability.takeCrit(self.mod, None, None)
        
        assert mod == self.mod, "Mod should not be altered."
        assert len(messages) == 0, "Should have no messages returned."
        
testcasesTakeCrit = ["properReturnValues"]
suiteTakeCrit = unittest.TestSuite(map(takeCrit, testcasesTakeCrit))

##########################################################

class effectivenessOnAttack(unittest.TestCase):
    """ Test that effectivenessOnAttack returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability(None)
        self.mod = 1
        
    def properReturnValues(self):
        """ Check that effectivenessOnAttack returns the proper default values """
        mod, message = self.ability.effectivenessOnAttack(None, None)
        
        assert mod == self.mod, "Mod should not be altered."
        assert message is None, "Should have no special message."
        
testcasesEffectivenessOnAttack = ["properReturnValues"]
suiteEffectivenessOnAttack = unittest.TestSuite(map(effectivenessOnAttack, testcasesEffectivenessOnAttack))

##########################################################

class effectivenessOnDefense(unittest.TestCase):
    """ Test that effectivenessOnDefense returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability(None)
        self.mod = 1
        
    def properReturnValues(self):
        """ Check that effectivenessOnDefense returns the proper default values """
        mod, message = self.ability.effectivenessOnDefense(None, None)
        
        assert mod == self.mod, "Mod should not be altered."
        assert message is None, "Should have no special message."
        
testcasesEffectivenessOnDefense = ["properReturnValues"]
suiteEffectivenessOnDefense = unittest.TestSuite(map(effectivenessOnDefense, testcasesEffectivenessOnDefense))

##########################################################

class onAccuracy(unittest.TestCase):
    """ Test that onAccuracy returns the correct default values """
    
    def setUp(self):
        """ Builds the ability """
        self.ability = Ability(None)
        self.accuracy = 90
        
    def properReturnValues(self):
        """ Check that onAccuracy returns the proper default values """
        accuracy = self.ability.onAccuracy(self.accuracy)
        assert accuracy == self.accuracy, "Accuracy should be unaltered."
        
testcasesOnAccuracy = ["properReturnValues"]
suiteOnAccuracy = unittest.TestSuite(map(onAccuracy, testcasesOnAccuracy))

##########################################################

class onContact(unittest.TestCase):
    """ Test that onContact returns the values """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.pkmn = BuildPokemonBattleWrapper()
        self.attacker = BuildPokemonBattleWrapper()
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that onContact returns the proper default values """
        messages = self.ability.onContact(self.pkmn, self.attacker)
        assert messages == [], "Should have no messages."
        
testcasesOnContact = ["properReturnValues"]
suiteOnContact = unittest.TestSuite(map(onContact, testcasesOnContact))

##########################################################

class onStab(unittest.TestCase):
    """ Test that onStab returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = Ability(None)
        
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
        self.ability = Ability(None)
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
        self.ability = Ability(None)
        
    def properReturnValues(self):
        """ Check that onStatus returns the proper default values """
        messages = self.ability.onStatus(None, None)
        
        assert len(messages) == 0, "Messages should have no elements"
        
testcasesOnStatus = ["properReturnValues"]
suiteOnStatus = unittest.TestSuite(map(onStatus, testcasesOnStatus))

##########################################################

 
suites = [suiteStopAttack, suiteAfterTurn, suiteCanUseEffects, suiteGiveCrit, suiteTakeCrit,\
          suiteEffectivenessOnAttack, suiteEffectivenessOnDefense, suiteOnAccuracy, suiteOnContact,
          suiteOnStab, suiteOnStatMod, suiteOnStatus, suiteCanBeConfused]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()