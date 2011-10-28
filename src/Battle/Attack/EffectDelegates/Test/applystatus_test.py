from Battle.Attack.EffectDelegates.applystatus_delegate import ApplyStatusDelegate

from Battle.Attack.attack import Attack
from Battle.battle_side import BattleSide
from Battle.Status.status import Status
from Battle.Status.paralysis import Paralysis
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually applies a status """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def appliesStatusUser(self):
        """ Tests if applyEffect applies the status to the user's side """
        self.delegate.affectUser = 1
        message = self.delegate.applyEffect(self.side, None)
        
        assert self.side.currPokemon.getStatus().abbr == self.status, "Status should be PAR on the user side"
        
testcasesApplyEffect = ["appliesStatusUser"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class applyStatus(unittest.TestCase):
    """ Test that applyStatus actually applies a status """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def appliesStatusUser(self):
        """ Tests if applyStatus applies the staus and returns the method """
        self.delegate.affectUser = 1
        self.delegate.applyStatus(self.side)
        assert self.side.currPokemon.getStatus().abbr == self.status, "Status should be PAR on the user side"
        
testcasesApplyStatus = ["appliesStatusUser"]
suiteApplyStatus = unittest.TestSuite(map(applyStatus, testcasesApplyStatus))

##########################################################

class checkStatusAlready(unittest.TestCase):
    """ Test that checkStatusAlready returns correctly """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.status = "PAR"
        attack = Attack()
        attack.type = ""
        self.delegate = ApplyStatusDelegate(attack, self.status, 1)
        
    def hasStatusAlready(self):
        """ Tests checkStatusAlready returns correctly if the side has a status already """
        self.side.currPokemon.setStatus(Paralysis())
        assert self.delegate.checkStatusAlready(self.side), "Should have a status already"
        
    def hasNoStatusAlready(self):
        """ Tests checkStatusAlready returns correctly if the side has a status already """
        self.side.currPokemon.setStatus(Status())
        assert not self.delegate.checkStatusAlready(self.side), "Should not have a status already"
        
testcasesCheckStatusAlready = ["hasStatusAlready", "hasNoStatusAlready"]
suiteCheckStatusAlready = unittest.TestSuite(map(checkStatusAlready, testcasesCheckStatusAlready))

##########################################################
 
suites = [suiteApplyEffect, suiteApplyStatus, suiteCheckStatusAlready]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()