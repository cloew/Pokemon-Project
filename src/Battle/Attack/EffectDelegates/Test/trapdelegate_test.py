from Battle.Attack.EffectDelegates.trap_delegate import TrapDelegate

from Battle.Attack.attack import Attack
from Battle.Attack.Trap.trap import Trap
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
        self.delegate = TrapDelegate("", "")
        
    def appliesTrap(self):
        """ Tests if applyEffect applies the trap """
        self.side.afterEffects = []
        self.delegate.applyEffect(None, self.side)
        
        assert isinstance(self.side.afterEffects[0], Trap), "Should have a trap effect"
        
testcasesApplyEffect = ["appliesTrap"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################
 
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()