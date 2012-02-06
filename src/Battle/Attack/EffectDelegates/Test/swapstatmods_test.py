from Battle.Attack.EffectDelegates.swapstatmods_delegate import SwapStatModsDelegate

from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
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
        
        side1 = BattleSide(trainer)
        self.wrapper1 = PkmnBattleWrapper(side1)
        self.wrapper1.pkmn = pokemon
        
        side2 = BattleSide(trainer)
        self.wrapper2 = PkmnBattleWrapper(side2)
        self.wrapper2.pkmn = pokemon
        
        self.delegate = SwapStatModsDelegate()
        
        self.statMods1 = {"ATK":1, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":1}
        self.wrapper1.statMods = self.statMods1
                                
        self.statMods2 = {"ATK":0, "DEF":0, "SPD":1, "SATK":1, "SDEF":1, 
                                "ACC":0, "EVAS":0, "CRT":0}
        self.wrapper2.statMods = self.statMods2
        
    def statModsSwitched(self):
        """ Tests if ithe stat mods are swapped """
        self.delegate.applyEffect(self.wrapper1, self.wrapper2)
        assert self.wrapper1.statMods == self.statMods2, "Pkmn 1 should have stats from Pkmn 2"
        assert self.wrapper2.statMods == self.statMods1, "Pkmn 2 should have stats from Pkmn 1"
        
testcasesApplyEffect= ["statModsSwitched"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################
 
suites = [suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()