import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.SecondaryEffects.trap import Trap
from Battle.Status.faint import Faint

class afterTurn(unittest.TestCase):
    """ Test that afterTurn returns correctly """
    
    def setUp(self):
        """ Builds the side and trap """
        self.source = BuildPokemonBattleWrapper()
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.message = " hurt."
        self.doneMessage = " done."
        self.trap = Trap(None, self.message, self.doneMessage)
    
    def turnDecreases(self):
        """ Test the turn counter decreases """
        self.trap.turns = 5
        turns = self.trap.turns
        self.trap.afterTurn(self.pkmn)
        assert self.trap.turns == turns - 1, "Turns should decrement"
        
    def effectIsRemoved(self):
        """ Test that the effect is removed when the turn count is reduced to zero """
        self.trap.turns = 1
        self.pkmn.secondaryEffects.append(self.trap)
        self.trap.afterTurn(self.pkmn)
        
        assert self.trap.turns == 0, "Turns should be zero"
        assert not self.trap in self.pkmn.secondaryEffects
        
    def message(self):
        """ Test the message is correct """
        message = self.trap.afterTurn(self.pkmn)
        assert message == [self.pkmn.getHeader() + self.message], "Message should be the pokemon's name and the message given to the Trap."
        
    def doneMessage(self):
        """ Test the done message is correct """
        self.trap.turns = 1
        self.pkmn.secondaryEffects.append(self.trap)
        messages = self.trap.afterTurn(self.pkmn)
        
        assert len(messages) == 2, "Should have two messages"
        assert messages[1] == self.pkmn.getHeader() + self.doneMessage, "Done message should be returned."
        
    def faintMessage(self):
        """ Test the faint message appears if the Pkmn faints """
        self.trap.turns = 3
        self.pkmn.setCurrHP(self.trap.getDamage(self.pkmn))
        
        self.pkmn.secondaryEffects.append(self.trap)
        messages = self.trap.afterTurn(self.pkmn)
        
        assert len(messages) == 2, "Should have two messages"
        assert messages[1] == self.pkmn.getHeader() + Faint.start, "Pkmn should have fainted."
    
    def faintAndDoneMessage(self):
        """ Test the done message is correct """
        self.trap.turns = 1
        self.pkmn.setCurrHP(self.trap.getDamage(self.pkmn))
        
        self.pkmn.secondaryEffects.append(self.trap)
        messages = self.trap.afterTurn(self.pkmn)
        
        assert len(messages) == 2, "Should have two messages"
        assert messages[1] == self.pkmn.getHeader() + Faint.start, "Pkmn should have fainted."
        
testcasesAfterTurn = ["turnDecreases", "effectIsRemoved", "message", "doneMessage", "faintMessage", "faintAndDoneMessage"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getDamage(unittest.TestCase):
    """ Test that getDamage returns the right amount of damage """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.pkmn = BuildPokemonBattleWrapper()
        self.trap = Trap(None, "", "")
        self.hp = 32.0
    
    def damage(self):
        """ Test the damage returns the proper ratio """
        self.pkmn.setStat("HP", self.hp)
        damage = self.trap.getDamage(self.pkmn)
        assert damage == self.hp/Trap.ratio, "Damage should be a sixteenth of the targets health"
        
testcasesGetDamage = ["damage"]
suiteGetDamage = unittest.TestSuite(map(getDamage, testcasesGetDamage))

##########################################################
 
suites = [suiteGetDamage, suiteAfterTurn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()