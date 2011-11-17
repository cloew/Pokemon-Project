from Battle.Attack.EffectDelegates.periodicheal_delegate import PeriodicHealDelegate

from Battle.Attack.attack import Attack
from Battle.SecondaryEffects.AfterTurnEffects.periodic_heal import PeriodicHeal
from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a Periodic Heal effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = PeriodicHealDelegate("", "")
        
    def appliesPeriodicHeal(self):
        """ Tests if applyEffect applies the heal """
        self.side.afterEffects = []
        self.delegate.applyEffect(self.side, None)
        
        assert isinstance(self.side.afterEffects[0], PeriodicHeal), "Should have a periodic heal effect"
        
testcasesApplyEffect = ["appliesPeriodicHeal"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousHeal(unittest.TestCase):
    """ Test that removePreviousHeal actually removes previous heal effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = PeriodicHealDelegate("", "")
        self.heal = PeriodicHeal("")
        
    def removesPeriodicHeal(self):
        """ Tests if removePreviousHeal actually removes the heal """
        self.side.afterEffects = [self.heal]
        self.delegate.removePreviousHeal(self.side)
        
        assert not self.heal in self.side.afterEffects, "Should not have the original periodic heal effect"
        
testcasesRemovePreviousHeal = ["removesPeriodicHeal"]
suiteRemovePreviousHeal = unittest.TestSuite(map(removePreviousHeal, testcasesRemovePreviousHeal))

##########################################################

class hasHeal(unittest.TestCase):
    """ Test that hasHeal returns appropriately for when there is and isn't periodic heal effects """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = PeriodicHealDelegate("", "")
        self.heal = PeriodicHeal("")
        
    def hasHeal(self):
        """ Tests if hasHeal returns true when there is a heal """
        self.side.afterEffects = [self.heal]
        
        assert self.delegate.hasHeal(self.side), "Should have a periodic heal effect"
        
    def noHeal(self):
        """ Tests if hasHeal returns false when there is no heal """
        self.side.afterEffects = []
        
        assert not self.delegate.hasHeal(self.side), "Should not have a periodic heal effect"
        
testcasesHasHeal = ["hasHeal", "noHeal"]
suiteHasHeal = unittest.TestSuite(map(hasHeal, testcasesHasHeal))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousHeal, suiteHasHeal]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()