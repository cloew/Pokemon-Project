from Battle.Attack.attack import Attack
from Battle.Attack.EffectDelegates.applystatus_delegate import ApplyStatusDelegate
from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate
from Battle.Attack.HitDelegates.statushit_delegate import StatusHitDelegate
from Battle.battle_side import BattleSide
from Battle.Status.status import Status
from Battle.Status.statusfactory import StatusFactory
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class immune(unittest.TestCase):
    """ Test that immune returns the correct values """
    
    def setUp(self):
        """ Build side for use in test cases """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.parent = Attack()
        self.parent.type ="NORMAL"
        
    def buildDelegate(self, effect):
        """ Builds a staushit delegate and its parent attack """
        self.parent.effectDelegates = [effect]
        self.delegate = StatusHitDelegate(self.parent, 100)
        
    def notImmune(self):
        """ Test an effect that is not immune returns correctly  """
        status = Status()
        self.side.currPokemon.setStatus(status)
        
        effect = ApplyStatusDelegate(self.parent, "PAR", 1)
        self.buildDelegate(effect)
        assert not self.delegate.immune(self.side, None), "Should not be immune"
    
    def immune(self):
        """ Test an effect that is immune will result in a miss """
        status, message = StatusFactory.buildStatusFromAbbr("PAR")
        self.side.currPokemon.setStatus(status)
        
        effect = ApplyStatusDelegate(self.parent, "PAR", 1)
        self.buildDelegate(effect)
        assert self.delegate.immune(self.side, None), "Should be immune"
        
    def noImmune(self):
        """ Test an effect that has no immune function isn't immune """
        effect = StatModDelegate("ATK", 1, 1)
        self.buildDelegate(effect)
        assert not  self.delegate.immune(self.side, None), "Should never be immune"
        
testcasesImmune= ["notImmune", "immune", "noImmune"]
suiteImmune= unittest.TestSuite(map(immune, testcasesImmune))

#########################################################
 
suites = [suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()