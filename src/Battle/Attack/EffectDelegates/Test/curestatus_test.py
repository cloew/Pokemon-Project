from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.curestatus_delegate import CureStatusDelegate

from Battle.Attack.attack import Attack
from Battle.Status.status import Status
from Battle.Status.paralysis import Paralysis

import unittest

class checkCurable(unittest.TestCase):
    """ Test that checkCurable actually cures a status when possible """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.wrapper = BuildPokemonBattleWrapper()
        
        self.statusAbbr = "PAR"
        self.status = Paralysis()
        self.statusAbbr2 = "FRZ"
        
        self.delegate = CureStatusDelegate(self.statusAbbr, 1)
        self.delegate2 = CureStatusDelegate(self.statusAbbr2, 1)
        
    def isCurable(self):
        """ Tests if checkCurable cures the status when it can """
        self.wrapper.setStatus(self.status)
        self.delegate.checkCurable(self.wrapper)
        
        assert self.wrapper.getStatus() != self.status, "Status should be cured"
        
    def notCurable(self):
        """ Tests if checkCurable cures the status when it can """
        self.wrapper.setStatus(self.status)
        self.delegate2.checkCurable(self.wrapper)
        
        assert self.wrapper.getStatus() == self.status, "Status should not be cured"
        
testcasescheckCurable = ["isCurable", "notCurable"]
suitecheckCurable = unittest.TestSuite(map(checkCurable, testcasescheckCurable))

##########################################################
 
suites = [suitecheckCurable]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()