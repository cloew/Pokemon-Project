import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Status.sleep import Sleep

class getTurns(unittest.TestCase):
    """ Test that getTurns returns the correct values """
    
    def setUp(self):
        """ Builds the Sleep status"""
        self.status = Sleep()
    
    def checkTurns(self):
        """ Test that getTurns returns between the min and max """
        turns = self.status.getTurns()
        
        assert turns >= Sleep.min, "Turns should be at least the minimum"
        assert turns <= Sleep.max, "Turns should be no gretaer than the max"
        
testcasesGetTurns = ["checkTurns"]
suiteGetTurns = unittest.TestSuite(map(getTurns, testcasesGetTurns))

##########################################################

class immobilized(unittest.TestCase):
    """ Test that immobilized performs correctly """
    
    def setUp(self):
        """ Builds the Sleep status"""
        self.status = Sleep()
        self.pkmn = BuildPokemonBattleWrapper()
        self.pkmn.setStatus(self.status)
        self.turns = 1
    
    def notDone(self):
        """ Test if immobilized returns correctly when it is not done """
        self.status.turns = self.turns
        
        immobilized, messages = self.status.immobilized(self.pkmn)
        
        assert immobilized, "Should be immobilized"
        assert messages == [self.pkmn.getHeader() + Sleep.intermittent],\
                "Should return Sleep's intermittent message"
        assert self.status.turns == self.turns - 1, "Turns should be decremented"
        
    def done(self):
        """ Test if immobilized returns correctly when it is done """
        self.status.turns = 0
        
        assert self.pkmn.getStatus() == self.status, "Should have status to start"
        
        immobilized, messages = self.status.immobilized(self.pkmn)
        
        assert not immobilized, "Should not be immobilized"
        assert len(messages) == 2, "Should have two messages"
        
        assert messages[0] == self.pkmn.getHeader() + Sleep.intermittent,\
                "Should return Sleep's intermittent message"
        assert messages[1] == self.pkmn.getHeader() + Sleep.done,\
                "Should return Sleep's done message"
                
        assert self.pkmn.getStatus() != self.status, "Status should be removed"
        
    
        
testcasesImmobilized = ["done", "notDone"]
suiteImmobilized= unittest.TestSuite(map(immobilized, testcasesImmobilized))

##########################################################
 
suites = [suiteGetTurns, suiteImmobilized]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()