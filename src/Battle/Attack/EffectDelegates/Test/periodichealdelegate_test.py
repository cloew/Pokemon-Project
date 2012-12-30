from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.periodicheal_delegate import PeriodicHealDelegate

from Battle.Attack.attack import Attack
from Battle.SecondaryEffects.periodic_heal import PeriodicHeal

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a Periodic Heal effect """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.pkmn  =  BuildPokemonBattleWrapper()
        self.delegate = PeriodicHealDelegate("", "")
        
    def appliesPeriodicHeal(self):
        """ Tests if applyEffect applies the heal """
        self.pkmn.secondaryEffects = []
        self.delegate.applyEffect(self.pkmn, None, None)
        
        assert isinstance(self.pkmn.secondaryEffects[0], PeriodicHeal), "Should have a periodic heal effect"
        
testcasesApplyEffect = ["appliesPeriodicHeal"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousHeal(unittest.TestCase):
    """ Test that removePreviousHeal actually removes previous heal effect """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.pkmn  =  BuildPokemonBattleWrapper()
        self.delegate = PeriodicHealDelegate("", "")
        self.heal = PeriodicHeal("")
        
    def removesPeriodicHeal(self):
        """ Tests if removePreviousHeal actually removes the heal """
        self.pkmn.secondaryEffects = [self.heal]
        self.delegate.removePreviousHeal(self.pkmn)
        
        assert not self.heal in self.pkmn.secondaryEffects, "Should not have the original periodic heal effect"
        
testcasesRemovePreviousHeal = ["removesPeriodicHeal"]
suiteRemovePreviousHeal = unittest.TestSuite(map(removePreviousHeal, testcasesRemovePreviousHeal))

##########################################################

class hasHeal(unittest.TestCase):
    """ Test that hasHeal returns appropriately for when there is and isn't periodic heal effects """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.pkmn  =  BuildPokemonBattleWrapper()
        self.delegate = PeriodicHealDelegate("", "")
        self.heal = PeriodicHeal("")
        
    def hasHeal(self):
        """ Tests if hasHeal returns true when there is a heal """
        self.pkmn.secondaryEffects = [self.heal]
        
        assert self.delegate.hasHeal(self.pkmn), "Should have a periodic heal effect"
        
    def noHeal(self):
        """ Tests if hasHeal returns false when there is no heal """
        self.pkmn.secondaryEffects = []
        
        assert not self.delegate.hasHeal(self.pkmn), "Should not have a periodic heal effect"
        
testcasesHasHeal = ["hasHeal", "noHeal"]
suiteHasHeal = unittest.TestSuite(map(hasHeal, testcasesHasHeal))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousHeal, suiteHasHeal]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()