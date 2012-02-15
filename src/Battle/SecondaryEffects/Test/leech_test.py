import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.SecondaryEffects.leech import Leech
from Pokemon.pokemon import Pokemon

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the Pkmn and the Leech Effect """
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.message = " hurt."
        self.pkmn2 = BuildPokemonBattleWrapper()
        self.leech = Leech(self.pkmn2, self.message)
        
    def message(self):
        """ Test the message is correct """
        message = self.leech.afterTurn(self.pkmn)
        assert message == [self.pkmn.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Leech."
        
testcasesAfterTurn = ["message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getAmount(unittest.TestCase):
    """ Test that getAmount returns the right amount to heal """
    
    def setUp(self):
        """ Builds the Pkmn and Leech """
        self.pkmn = BuildPokemonBattleWrapper()
        self.pkmn2 = BuildPokemonBattleWrapper()
        self.leech = Leech(self.pkmn2, "")
        self.hp = 32
    
    def amount(self):
        """ Test the heal returns the proper ratio """
        self.pkmn.setStat("HP", self.hp)
        amount = self.leech.getAmount(self.pkmn)
        assert amount == self.hp/Leech.ratio, "Amount should be a sixteenth of the targets health"
        
testcasesGetAmount = ["amount"]
suiteGetAmount = unittest.TestSuite(map(getAmount, testcasesGetAmount))

##########################################################
 
suites = [suiteGetAmount, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()