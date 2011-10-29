from Battle.AfterTurnEffects.trap import Trap
from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the side and trap """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        
        self.message = " hurt."
        self.trap = Trap(self.message)
    
    def turnDecreases(self):
        """ Test the turn counter decreases """
        turns = self.trap.turns
        self.trap.afterTurn(self.side)
        assert self.trap.turns == turns - 1, "Turns should decrement"
        
    def message(self):
        """ Test the message is correct """
        message = self.trap.afterTurn(self.side)
        assert message == [self.side.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Trap."
        
testcasesAfterTurn = ["turnDecreases", "message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getDamage(unittest.TestCase):
    """ Test that getDamage returns the right amount of damage """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.pokemon = Pokemon("BULBASAUR")
        self.trap = Trap("")
        self.hp = 32.0
    
    def damage(self):
        """ Test the damage returns the proper ratio """
        self.pokemon.battleDelegate.stats["HP"] = self.hp
        damage = self.trap.getDamage(self.pokemon)
        assert damage == self.hp/Trap.ratio, "Damage should be a sixteenth of the targets health"
        
testcasesGetDamage = ["damage"]
suiteGetDamage = unittest.TestSuite(map(getDamage, testcasesGetDamage))

##########################################################
 
suites = [suiteGetDamage, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()