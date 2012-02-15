from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.leech_delegate import LeechDelegate

from Battle.Attack.attack import Attack
from Battle.SecondaryEffects.leech import Leech

import unittest

class applyEffect(unittest.TestCase):
    """ Test that applyEffect actually adds a leech effect """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.user = BuildPokemonBattleWrapper(pkmn = "CHARMANDER")
        self.target = BuildPokemonBattleWrapper(pkmn = "CHARMANDER")
        self.target2 = BuildPokemonBattleWrapper(pkmn = "BULBASAUR")
        
        self.delegate = LeechDelegate("", "", "FIRE")
        
    def appliesLeech(self):
        """ Tests if applyEffect applies the leech """
        self.target.secondaryEffects = []
        self.delegate.applyEffect(self.user, self.target)
        
        assert isinstance(self.target.secondaryEffects[0], Leech), "Target should have a Leech effect"
        assert self.target.secondaryEffects[0].source is self.user, "Leech should have the Pkmn as the Leech's Source"
        
    def immune(self):
        """ Tests if applyEffect applies the leech """
        self.target2.secondaryEffects = []
        self.delegate.applyEffect(self.user, self.target2)
        
        assert len(self.target2.secondaryEffects) == 0, "Should have no Leech effects when the target is immune"
        
testcasesApplyEffect = ["appliesLeech", "immune"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class removePreviousLeech(unittest.TestCase):
    """ Test that removePreviousLeech actually removes a leech effect """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.wrapper = BuildPokemonBattleWrapper()
        self.delegate = LeechDelegate("", "", "FIRE")
        self.leech = Leech(None, "")
        
    def removeLeech(self):
        """ Tests if the leech is removed """
        self.wrapper.secondaryEffects = [self.leech]
        self.delegate.removePreviousLeech(self.wrapper)
        
        assert not self.leech in self.wrapper.secondaryEffects, "Should have removed original trap effect"
        
testcasesRemovePreviousLeech = ["removeLeech"]
suiteRemovePreviousLeech = unittest.TestSuite(map(removePreviousLeech, testcasesRemovePreviousLeech))

##########################################################

class hasThisLeech(unittest.TestCase):
    """ Test that hasThisLeech actually returns when it has that type of trap """
    
    def setUp(self):
        """ Builds the delegate and pkmn for use in the tests """
        self.wrapper = BuildPokemonBattleWrapper()
        self.delegate = LeechDelegate("", "", "FIRE")
        self.leech = Leech(None, "")
        self.otherLeech = Leech(None, "other.")
        
    def hasLeech(self):
        """ Tests if hasThisLeech returns true when there is an object of this leech """
        self.wrapper.secondaryEffects = [self.leech]
        
        assert self.delegate.hasThisLeech(self.wrapper), "Should have a leech effect"
        
    def noLeech(self):
        """ Tests if hasThisLeech returns false when there is no trap """
        self.wrapper.secondaryEffects = []
        
        assert not self.delegate.hasThisLeech(self.wrapper), "Should not have a leech effect"
        
    def otherLeech(self):
        """ Tests if hasThisLeech returns false when there is a different leech """
        self.wrapper.secondaryEffects = [self.otherLeech]
        
        assert not self.delegate.hasThisLeech(self.wrapper), "Should not have a leech effect if there is a different leech effect there"
        
testcasesHasThisLeech = ["hasLeech", "noLeech", "otherLeech"]
suiteHasThisLeech = unittest.TestSuite(map(hasThisLeech, testcasesHasThisLeech))

##########################################################
 
suites = [suiteApplyEffect, suiteRemovePreviousLeech, suiteHasThisLeech]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()