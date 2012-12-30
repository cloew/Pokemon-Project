import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.trap_delegate import TrapDelegate
from Battle.SecondaryEffects.trap import Trap

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a trap effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = TrapDelegate("", "", "")
        
    def appliesTrap(self):
        """ Tests if applyEffect applies the trap """
        self.pkmn.secondaryEffects = []
        self.delegate.applyEffect(None, self.pkmn, None)
        
        assert isinstance(self.pkmn.secondaryEffects[0], Trap), "Should have a trap effect"
        
testcasesApplyEffect = ["appliesTrap"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousTrap(unittest.TestCase):
    """ Test that removePreviousTrap actually removes a trap effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = TrapDelegate("", "", "")
        self.trap = Trap(None, "", "")
        
    def removeTrap(self):
        """ Tests if the trap is removed """
        self.pkmn.secondaryEffects = [self.trap]
        self.delegate.removePreviousTrap(self.pkmn)
        
        assert not self.trap in self.pkmn.secondaryEffects, "Should have removed original trap effect"
        
testcasesRemovePreviousTrap = ["removeTrap"]
suiteRemovePreviousTrap = unittest.TestSuite(map(removePreviousTrap, testcasesRemovePreviousTrap))

##########################################################

class hasThisTrap(unittest.TestCase):
    """ Test that hasThisTrap actually returns when it has that type of trap """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = TrapDelegate("", "", "")
        self.trap = Trap(None, "", "")
        self.otherTrap = Trap(None, "other.", "")
        
    def hasTrap(self):
        """ Tests if hasThisTrap returns true when there is an object of this trap """
        self.pkmn.secondaryEffects = [self.trap]
        
        assert self.delegate.hasThisTrap(self.pkmn), "Should have a trap effect"
        
    def noTrap(self):
        """ Tests if hasThisTrap returns false when there is no trap """
        self.pkmn.secondaryEffects = []
        
        assert not self.delegate.hasThisTrap(self.pkmn), "Should not have a trap effect"
        
    def otherTrap(self):
        """ Tests if hasThisTrap returns false when there is a different trap """
        self.pkmn.secondaryEffects = [self.otherTrap]
        
        assert not self.delegate.hasThisTrap(self.pkmn), "Should not have a trap effect if there is a different trap effect there"
        
testcasesHasThisTrap = ["hasTrap", "noTrap", "otherTrap"]
suiteHasThisTrap = unittest.TestSuite(map(hasThisTrap, testcasesHasThisTrap))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousTrap, suiteHasThisTrap]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()