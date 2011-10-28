from Battle.Attack.EffectDelegates.swapstatmods_delegate import SwapStatModsDelegate

from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class applyEffect(unittest.TestCase):
    """ Test that isCharging returns the correct values """
    def setUp(self):
        """ Grabs the message dictionary from StatModDelegate """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side1 = BattleSide(trainer)
        self.side2 = BattleSide(trainer)
        self.delegate = SwapStatModsDelegate()
        
        self.statMods1 = {"ATK":1, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":1}
        self.side1.statMods = self.statMods1
                                
        self.statMods2 = {"ATK":0, "DEF":0, "SPD":1, "SATK":1, "SDEF":1, 
                                "ACC":0, "EVAS":0, "CRT":0}
        self.side2.statMods = self.statMods2
        
    def statModsSwitched(self):
        """ Tests if ithe stat mods are swapped """
        self.delegate.applyEffect(self.side1, self.side2)
        assert self.side1.statMods == self.statMods2, "Side1 should have stats from side2"
        assert self.side2.statMods == self.statMods1, "Side2 should have stats from side1"
        
testcasesApplyEffect= ["statModsSwitched"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################
 
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()