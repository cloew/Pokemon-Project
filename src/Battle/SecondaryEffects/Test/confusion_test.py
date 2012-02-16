import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from  Battle.SecondaryEffects.confusion import Confusion

class checkOver(unittest.TestCase):
    """ Test cases of checkOver """
    
    def  setUp(self):
        """ Build the Confusion for the test """
        self.user = BuildPokemonBattleWrapper()
        self.confusion = Confusion()
        self.turns = 2
        
    def overCured(self):
        """ Test that the Confusion is cured when it is over """
        messages = []
        self.confusion.turns = 0
        self.user.secondaryEffects = [self.confusion]
        self.confusion.checkOver(self.user, messages)
        
        assert self.user.secondaryEffects == [], "Should be cured"
        
    def overMessage(self):
        """ Test that the Message is correct when it is over """
        messages = []
        self.confusion.turns = 0
        self.user.secondaryEffects = [self.confusion]
        message = self.user.getHeader() + Confusion.over
        self.confusion.checkOver(self.user, messages)
        
        assert len(messages) == 1, "Should receive one message"
        assert messages[0] == message, "Should receive a message that the confusion is over"
    
    def notOverStillConfused(self):
        """ Test that thePkmn is still confused when it isn't over """
        messages = []
        self.confusion.turns = self.turns
        self.user.secondaryEffects = [self.confusion]
        self.confusion.checkOver(self.user, messages)
        
        assert self.user.secondaryEffects == [self.confusion], "Should still be confused"

    def notOverTurnsDecremented(self):
        """ Test that the Turns is decremented when it isn't over """
        messages = []
        self.confusion.turns = self.turns
        self.confusion.checkOver(self.user, messages)
        
        assert self.confusion.turns == self.turns-1, "Should have turns decremented"

    def notOverMessage(self):
        """ Test that the Message is correct when it isn't over """
        messages = []
        self.confusion.turns = self.turns
        message = self.user.getHeader() + Confusion.start
        self.confusion.checkOver(self.user, messages)
        
        assert len(messages) == 1, "Should receive one message"
        assert messages[0] == message, "Should receive a message that the Pkmn is still confusion"

# Collect all test cases in this class
testcasesCheckOver = ["overCured", "overMessage", "notOverStillConfused", "notOverTurnsDecremented", "notOverMessage"]
suiteCheckOver = unittest.TestSuite(map(checkOver, testcasesCheckOver))

##########################################################

class cure(unittest.TestCase):
    """ Test cases of cure """
    
    def  setUp(self):
        """ Build the Confusion for the test """
        self.user = BuildPokemonBattleWrapper()
        self.confusion = Confusion()
        
    def cured(self):
        """ Test that the Confusion is cured"""
        self.user.secondaryEffects = [self.confusion]
        self.confusion.cure(self.user)
        assert self.user.secondaryEffects == [], "Should be cured"

# Collect all test cases in this class
testcasesCure = ["cured"]
suiteCure = unittest.TestSuite(map(cure, testcasesCure))

##########################################################

class confused(unittest.TestCase):
    """ Test cases of confused """
    
    def  setUp(self):
        """ Build the Confusion for the test """
        self.confusion = Confusion()
        
    def isConfused(self):
        """ Test that Pkmn is confused on 1 """
        confused = self.confusion.confused(1)
        assert confused, "Should be confused"
        
    def notConfused(self):
        """ Test that Pkmn is not confused on 1 """
        confused = self.confusion.confused(0)
        assert not confused, "Should be confused"

# Collect all test cases in this class
testcasesConfused = ["isConfused", "notConfused"]
suiteConfused = unittest.TestSuite(map(confused, testcasesConfused))

##########################################################

# Collect all test cases in this file
suites = [suiteCheckOver, suiteCure, suiteConfused]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()