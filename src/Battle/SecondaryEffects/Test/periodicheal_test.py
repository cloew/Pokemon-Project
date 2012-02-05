from Battle.SecondaryEffects.periodic_heal import PeriodicHeal
from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the side and heal """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        side = BattleSide(trainer)
        self.wrapper = PkmnBattleWrapper(side)
        self.wrapper.pkmn = pokemon
        
        self.message = " hurt."
        self.heal = PeriodicHeal(self.message)
        
    def message(self):
        """ Test the message is correct """
        message = self.heal.afterTurn(self.wrapper)
        assert message == [self.wrapper.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Heal."
        
testcasesAfterTurn = ["message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getHeal(unittest.TestCase):
    """ Test that getHeal returns the right amount to heal """
    
    def setUp(self):
        """ Builds the heal """
        self.pokemon = Pokemon("BULBASAUR")
        self.heal = PeriodicHeal("")
        self.hp = 32.0
    
    def heal(self):
        """ Test the heal returns the proper ratio """
        self.pokemon.battleDelegate.stats["HP"] = self.hp
        heal = self.heal.getHeal(self.pokemon)
        assert heal == self.hp/PeriodicHeal.ratio, "Heal should be a sixteenth of the targets health"
        
testcasesGetHeal = ["heal"]
suiteGetHeal = unittest.TestSuite(map(getHeal, testcasesGetHeal))

##########################################################
 
suites = [suiteGetHeal, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()