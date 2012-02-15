import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.SecondaryEffects.periodic_heal import PeriodicHeal

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Build the Pkmn and Heal """
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.message = " hurt."
        self.heal = PeriodicHeal(self.message)
        
    def message(self):
        """ Test the message is correct """
        message = self.heal.afterTurn(self.pkmn)
        assert message == [self.pkmn.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Heal."
        
testcasesAfterTurn = ["message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getHeal(unittest.TestCase):
    """ Test that getHeal returns the right amount to heal """
    
    def setUp(self):
        """ Builds the heal """
        self.pkmn = BuildPokemonBattleWrapper()
        self.heal = PeriodicHeal("")
        self.hp = 32
    
    def heal(self):
        """ Test the heal returns the proper ratio """
        self.pkmn.setStat("HP", self.hp)
        heal = self.heal.getHeal(self.pkmn)
        assert heal == self.hp/PeriodicHeal.ratio, "Heal should be a sixteenth of the targets health"
        
testcasesGetHeal = ["heal"]
suiteGetHeal = unittest.TestSuite(map(getHeal, testcasesGetHeal))

##########################################################
 
suites = [suiteGetHeal, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()