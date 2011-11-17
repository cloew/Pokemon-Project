from Battle.Attack.EffectDelegates.leech_delegate import LeechDelegate

from Battle.Attack.attack import Attack
from Battle.SecondaryEffects.leech import Leech
from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a leech effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        trainer2 = Trainer()
        pokemon = Pokemon("CHARMANDER")
        pokemon2 = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        trainer2.beltPokemon = [pokemon2]
        self.side = BattleSide(trainer)
        self.side2 = BattleSide(trainer2)
        self.delegate = LeechDelegate("", "", "FIRE")
        
    def appliesLeech(self):
        """ Tests if applyEffect applies the leech """
        self.side.secondaryEffects = []
        self.delegate.applyEffect(self.side2, self.side)
        
        assert isinstance(self.side.secondaryEffects[0], Leech), "Should have a Leech effect"
        
    def immune(self):
        """ Tests if applyEffect applies the leech """
        self.side2.secondaryEffects = []
        self.delegate.applyEffect(self.side, self.side2)
        
        assert len(self.side2.secondaryEffects) == 0, "Should have no Leech effects when the target is immune"
        
testcasesApplyEffect = ["appliesLeech", "immune"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousLeech(unittest.TestCase):
    """ Test that removePreviousLeech actually removes a leech effect """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = LeechDelegate("", "", "FIRE")
        self.leech = Leech(None, "")
        
    def removeLeech(self):
        """ Tests if the leech is removed """
        self.side.secondaryEffects = [self.leech]
        self.delegate.removePreviousLeech(self.side)
        
        assert not self.leech in self.side.secondaryEffects, "Should have removed original trap effect"
        
testcasesRemovePreviousLeech = ["removeLeech"]
suiteRemovePreviousLeech = unittest.TestSuite(map(removePreviousLeech, testcasesRemovePreviousLeech))

##########################################################

class hasThisLeech(unittest.TestCase):
    """ Test that hasThisLeech actually returns when it has that type of trap """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = LeechDelegate("", "", "FIRE")
        self.leech = Leech(None, "")
        self.otherLeech = Leech(None, "other.")
        
    def hasLeech(self):
        """ Tests if hasThisLeech returns true when there is an object of this leech """
        self.side.secondaryEffects = [self.leech]
        
        assert self.delegate.hasThisLeech(self.side), "Should have a leech effect"
        
    def noLeech(self):
        """ Tests if hasThisLeech returns false when there is no trap """
        self.side.secondaryEffects = []
        
        assert not self.delegate.hasThisLeech(self.side), "Should not have a leech effect"
        
    def otherLeech(self):
        """ Tests if hasThisLeech returns false when there is a different leech """
        self.side.secondaryEffects = [self.otherLeech]
        
        assert not self.delegate.hasThisLeech(self.side), "Should not have a leech effect if there is a different leech effect there"
        
testcasesHasThisLeech = ["hasLeech", "noLeech", "otherLeech"]
suiteHasThisLeech = unittest.TestSuite(map(hasThisLeech, testcasesHasThisLeech))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousLeech, suiteHasThisLeech]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()