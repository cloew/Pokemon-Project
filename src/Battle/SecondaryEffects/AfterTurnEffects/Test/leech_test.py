from Battle.SecondaryEffects.AfterTurnEffects.leech import Leech
from Battle.battle_side import BattleSide
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the side and the leech """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        self.pokemon2 = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        
        self.message = " hurt."
        self.leech = Leech(self.pokemon2, self.message)
        
    def message(self):
        """ Test the message is correct """
        message = self.leech.afterTurn(self.side)
        assert message == [self.side.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Leech."
        
testcasesAfterTurn = ["message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getAmount(unittest.TestCase):
    """ Test that getAmount returns the right amount to heal """
    
    def setUp(self):
        """ Builds the heal """
        self.pokemon = Pokemon("BULBASAUR")
        self.pokemon2 = Pokemon("BULBASAUR")
        self.leech = Leech(self.pokemon2, "")
        self.hp = 32.0
    
    def amount(self):
        """ Test the heal returns the proper ratio """
        self.pokemon.battleDelegate.stats["HP"] = self.hp
        amount = self.leech.getAmount(self.pokemon)
        assert amount == self.hp/Leech.ratio, "Amount should be a sixteenth of the targets health"
        
testcasesGetAmount = ["amount"]
suiteGetAmount = unittest.TestSuite(map(getAmount, testcasesGetAmount))

##########################################################
 
suites = [suiteGetAmount, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()