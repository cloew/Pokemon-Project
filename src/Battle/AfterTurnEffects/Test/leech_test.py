import unittest
from Test.test_helper import BuildPokemon, BuildPokemonBattleWrapper

from Battle.AfterTurnEffects.leech import Leech
from Battle.Status.faint import Faint

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the side and the leech """
        self.pkmn2 = BuildPokemon()
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.message = " hurt."
        self.leech = Leech(self.pkmn2, self.message)
        
    def message(self):
        """ Test the message is correct """
        message = self.leech.afterTurn(self.pkmn)
        assert message == [self.pkmn.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Leech."
        
    def faint(self):
        """ Test that the messsages returned when the target faints """
        self.pkmn.setCurrHP(self.leech.getAmount(self.pkmn))
        messages = self.leech.afterTurn(self.pkmn)
        assert len(messages) == 2, "Should have 2 messages"
        assert messages[1] == self.pkmn.getHeader() + Faint.start, "Should have a faint message."
        
        
testcasesAfterTurn = ["message", "faint"]
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