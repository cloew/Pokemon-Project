from Battle.Attack.HitDelegates.piercedodge_delegate import PierceDodgeDelegate
from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class dodging(unittest.TestCase):
    """ Test that dodging returns the correct values """
    def setUp(self):
        """ Build side for use in test cases """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.pierce = "DIG"
        self.delegate = PierceDodgeDelegate(None, 100, "", self.pierce)
    
    def dodging(self):
        """ Test dodging function returns true correctly when the opp is dodging """
        self.side.dodge = "FLY"
        assert self.delegate.dodging(self.side), "Opp side should be dodging"
        
    def notDodging(self):
        """ Test dodging function returns false when the opp is not dodging """
        self.side.dodge = None
        assert not  self.delegate.dodging(self.side), "Opp side should not be dodging"
        
    def piercing(self):
        """ Test dodging function returns true correctly when piercing the opps dodge """
        self.side.dodge = self.pierce
        assert not  self.delegate.dodging(self.side), \
                "Opp side should be dodging, but the user should pierce"
        
testcasesDodging= ["dodging", "notDodging", "piercing"]
suiteDodging= unittest.TestSuite(map(dodging, testcasesDodging))

#########################################################
 
suites = [suiteDodging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()