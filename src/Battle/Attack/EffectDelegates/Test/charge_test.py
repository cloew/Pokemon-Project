from Battle.Attack.EffectDelegates.charge_delegate import ChargeDelegate

from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class isCharging(unittest.TestCase):
    """ Test that isCharging returns the correct values """
    def setUp(self):
        """ Grabs the message dictionary from StatModDelegate """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = ChargeDelegate(2, 0, "")
        
    def isCharging(self):
        """ Tests if isCHarging returns correctly when it is charging """
        self.delegate.turnOn = 1
        assert self.delegate.isCharging(self.side), "Should be charging"
        
    def isNotCharging(self):
        """ Tests if isCHarging returns correctly when it is not charging """
        self.delegate.turnOn = 0
        assert not self.delegate.isCharging(self.side), "Should not be charging"
        
testcasesIsCharging = ["isCharging", "isNotCharging"]
suiteIsCharging = unittest.TestSuite(map(isCharging, testcasesIsCharging))

##########################################################
 
suites = [suiteIsCharging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()