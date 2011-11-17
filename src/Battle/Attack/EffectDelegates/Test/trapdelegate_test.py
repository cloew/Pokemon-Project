from Battle.Attack.EffectDelegates.trap_delegate import TrapDelegate

from Battle.Attack.attack import Attack
from Battle.SecondaryEffects.trap import Trap
from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a trap effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = TrapDelegate("", "", "")
        
    def appliesTrap(self):
        """ Tests if applyEffect applies the trap """
        self.side.secondaryEffects = []
        self.delegate.applyEffect(None, self.side)
        
        assert isinstance(self.side.secondaryEffects[0], Trap), "Should have a trap effect"
        
testcasesApplyEffect = ["appliesTrap"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousTrap(unittest.TestCase):
    """ Test that removePreviousTrap actually removes a trap effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = TrapDelegate("", "", "")
        self.trap = Trap("", "")
        
    def removeTrap(self):
        """ Tests if the trap is removed """
        self.side.secondaryEffects = [self.trap]
        self.delegate.removePreviousTrap(self.side)
        
        assert not self.trap in self.side.secondaryEffects, "Should have removed original trap effect"
        
testcasesRemovePreviousTrap = ["removeTrap"]
suiteRemovePreviousTrap = unittest.TestSuite(map(removePreviousTrap, testcasesRemovePreviousTrap))

##########################################################

class hasThisTrap(unittest.TestCase):
    """ Test that hasThisTrap actually returns when it has that type of trap """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = TrapDelegate("", "", "")
        self.trap = Trap("", "")
        self.otherTrap = Trap("other.", "")
        
    def hasTrap(self):
        """ Tests if hasThisTrap returns true when there is an object of this trap """
        self.side.secondaryEffects = [self.trap]
        
        assert self.delegate.hasThisTrap(self.side), "Should have a trap effect"
        
    def noTrap(self):
        """ Tests if hasThisTrap returns false when there is no trap """
        self.side.secondaryEffects = []
        
        assert not self.delegate.hasThisTrap(self.side), "Should not have a trap effect"
        
    def otherTrap(self):
        """ Tests if hasThisTrap returns false when there is a different trap """
        self.side.secondaryEffects = [self.otherTrap]
        
        assert not self.delegate.hasThisTrap(self.side), "Should not have a trap effect if there is a different trap effect there"
        
testcasesHasThisTrap = ["hasTrap", "noTrap", "otherTrap"]
suiteHasThisTrap = unittest.TestSuite(map(hasThisTrap, testcasesHasThisTrap))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousTrap, suiteHasThisTrap]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()