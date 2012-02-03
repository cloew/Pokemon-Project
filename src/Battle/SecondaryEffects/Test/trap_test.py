from Battle.SecondaryEffects.trap import Trap
from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
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
        side = BattleSide(trainer)
        self.pkmnWrapper = PkmnBattleWrapper(side)
        self.pkmnWrapper.sendOutPkmn(pokemon)
        
        self.message = " hurt."
        self.doneMessage = " done."
        self.trap = Trap(self.message, self.doneMessage)
    
    def turnDecreases(self):
        """ Test the turn counter decreases """
        self.trap.turns = 5
        turns = self.trap.turns
        self.trap.afterTurn(self.pkmnWrapper)
        assert self.trap.turns == turns - 1, "Turns should decrement"
        
    def effectIsRemoved(self):
        """ Test that the effect is removed when the turn count is reduced to zero """
        self.trap.turns = 1
        self.pkmnWrapper.secondaryEffects.append(self.trap)
        self.trap.afterTurn(self.pkmnWrapper)
        
        assert self.trap.turns == 0, "Turns should be zero"
        assert not self.trap in self.pkmnWrapper.secondaryEffects
        
    def message(self):
        """ Test the message is correct """
        message = self.trap.afterTurn(self.pkmnWrapper)
        assert message == [self.pkmnWrapper.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Trap."
        
    def doneMessage(self):
        """ Test the done message is correct """
        self.trap.turns = 1
        self.pkmnWrapper.secondaryEffects.append(self.trap)
        messages = self.trap.afterTurn(self.pkmnWrapper)
        
        assert len(messages) == 2, "Should have two messages"
        assert messages[1] == self.pkmnWrapper.getHeader() + self.doneMessage, "Done message should be returned."
        
testcasesAfterTurn = ["turnDecreases", "effectIsRemoved", "message", "doneMessage"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getDamage(unittest.TestCase):
    """ Test that getDamage returns the right amount of damage """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.pokemon = Pokemon("BULBASAUR")
        self.trap = Trap("", "")
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