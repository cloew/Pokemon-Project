import unittest

from Battle.Attack.attackfactory import AttackFactory
from Pokemon.pokemon import Pokemon
from Trainer.computer_trainer import ComputerTrainer


class getAction(unittest.TestCase):
    """ Test cases of getFirstPokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = ComputerTrainer()
        self.poke= Pokemon("BULBASAUR")
        self.attack = AttackFactory.getAttackAsNew("TACKLE")
        self.poke.battleDelegate.attacks = [self.attack]
        
    def actionIsAttack(self):
        """ Check that the attack returned by getAction is an attack the Pokemon has """
        attackAction = self.trainer.getAction(self.poke)
        assert attackAction.attack is self.attack, "Should be the attack"

# Collect all test cases in this class
testcasesGetAction = ["actionIsAttack"]
suiteGetAction  = unittest.TestSuite(map(getAction, testcasesGetAction))

##########################################################

class getHeader(unittest.TestCase):
    """ Test cases of getFirstPokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = ComputerTrainer()
        
    def headerIsCompHeader(self):
        """ Check that the attack returned by getAction is an attack the Pokemon has """
        assert self.trainer.getHeader() is ComputerTrainer.header, "Should be 'Enemy '"

# Collect all test cases in this class
testcasesGetHeader = ["headerIsCompHeader"]
suiteGetHeader   = unittest.TestSuite(map(getHeader , testcasesGetHeader ))

##########################################################
# Collect all test cases in this file
suites = [suiteGetAction, suiteGetHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()