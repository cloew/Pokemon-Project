from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.applystatus_delegate import ApplyStatusDelegate

from Battle.Attack.attack import Attack
from Battle.Status.status import Status
from Battle.Status.paralysis import Paralysis

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually applies a status """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.battlePokemon = BuildPokemonBattleWrapper()
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def appliesStatusUser(self):
        """ Tests if applyEffect applies the status to the user's pkmn """
        self.delegate.affectUser = 1
        message = self.delegate.applyEffect(self.battlePokemon, None)
        
        assert self.battlePokemon.getStatus().abbr == self.status, "Status should be PAR on the user pkmn"
        
testcasesApplyEffect = ["appliesStatusUser"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class applyStatus(unittest.TestCase):
    """ Test that applyStatus actually applies a status """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.battlePokemon = BuildPokemonBattleWrapper()
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def appliesStatusUser(self):
        """ Tests if applyStatus applies the staus and returns the method """
        self.delegate.affectUser = 1
        self.delegate.applyStatus(self.battlePokemon)
        assert self.battlePokemon.getStatus().abbr == self.status, "Status should be PAR on the user pkmn"
        
testcasesApplyStatus = ["appliesStatusUser"]
suiteApplyStatus = unittest.TestSuite(map(applyStatus, testcasesApplyStatus))

##########################################################

class checkStatusAlready(unittest.TestCase):
    """ Test that checkStatusAlready returns correctly """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.battlePokemon = BuildPokemonBattleWrapper()
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def hasStatusAlready(self):
        """ Tests checkStatusAlready returns correctly if the pkmn has a status already """
        self.battlePokemon.setStatus(Paralysis())
        assert self.delegate.checkStatusAlready(self.battlePokemon), "Should have a status already"
        
    def hasNoStatusAlready(self):
        """ Tests checkStatusAlready returns correctly if the pkmn has a status already """
        self.battlePokemon.setStatus(Status())
        assert not self.delegate.checkStatusAlready(self.battlePokemon), "Should not have a status already"
        
testcasesCheckStatusAlready = ["hasStatusAlready", "hasNoStatusAlready"]
suiteCheckStatusAlready = unittest.TestSuite(map(checkStatusAlready, testcasesCheckStatusAlready))

##########################################################
 
suites = [suiteApplyEffect, suiteApplyStatus, suiteCheckStatusAlready]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()