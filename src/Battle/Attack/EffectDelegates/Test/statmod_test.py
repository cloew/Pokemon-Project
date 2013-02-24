from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate
from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class checkNoChange(unittest.TestCase):
    """ Test that checkNoChange returns the correct values """
    
    def setUp(self):
        """ Builds the BattleSide """
        self.stat = "ATK"
        self.pkmn =  BuildPokemonBattleWrapper()
        
    def buildStatModDelegate(self, degree):
        """ Returns a stat mod delegate with the given degree """
        return StatModDelegate(self.stat, degree, 1)
        
    def change_ModRaise(self):
        """ Test that a mod raise can return as a change"""
        self.pkmn.statMods[self.stat] = 0
        delegate = self.buildStatModDelegate(1)
        
        noChange, messages = delegate.checkNoChange(self.pkmn, 1)
        
        assert not noChange, "Change when the mod can raise"
        assert len(messages) == 0, "Should return no messages"
        
    def change_ModLower(self):
        """ Test that a mod lower can return as a change"""
        self.pkmn.statMods[self.stat] = 0
        delegate = self.buildStatModDelegate(-1)
        
        noChange, messages = delegate.checkNoChange(self.pkmn, -1)
        
        assert not noChange, "Change when the mod can lower"
        assert len(messages) == 0, "Should return no messages"
        
    def noChange_modZero(self):
        """ Test that a mod of zero returns as no change """
        self.pkmn.statMods[self.stat] = 0
        delegate = self.buildStatModDelegate(0)
        
        noChange, messages = delegate.checkNoChange(self.pkmn, 0)
        
        assert noChange, "No change when degree is 0"
        assert messages == [], "Should return no messages"
        
    def noChange_modTooHigh(self):
        """ Test that a mod that can't raise returns as no change """
        self.pkmn.statMods[self.stat] = 6
        delegate = self.buildStatModDelegate(2)
        
        noChange, messages = delegate.checkNoChange(self.pkmn, 2)
        
        assert noChange, "No change when degree is 0"
        find = messages[0].find(StatModDelegate.noChangeUp)
        assert not find == -1,"Should contain the message for going too high"
        
    def noChange_modTooLow(self):
        """ Test that a mod that can't lower returns as no change """
        self.pkmn.statMods[self.stat] = -6
        delegate = self.buildStatModDelegate(-2)
        
        noChange, messages = delegate.checkNoChange(self.pkmn, -2)
        
        assert noChange, "No change when degree is 0"
        find = messages[0].find(StatModDelegate.noChangeDown)
        assert not find == -1, "Should contain the message for going too low"
        
testcasesCheckNoChange = ["change_ModRaise", "change_ModLower", "noChange_modZero", "noChange_modTooHigh", "noChange_modTooLow"]
suiteCheckNoChange = unittest.TestSuite(map(checkNoChange, testcasesCheckNoChange))

##########################################################

class getMessage(unittest.TestCase):
    """ Test that getMessage returns the correct values """
    
    def setUp(self):
        """ Grabs the message dictionary from StatModDelegate """
        self.riseOrFall = StatModDelegate.riseOrFall
        self.sharply = StatModDelegate.sharply
        
    def buildStatModDelegate(self, degree):
        """ Returns a stat mod delegate with the given degree """
        return StatModDelegate(None, degree, None)
    

    def degree1(self):
        """ test message with satt mod change of 1 """
        delegate = self.buildStatModDelegate(1)
        message = delegate.getMessage()
        realMessage = self.riseOrFall[True] + self.sharply[1]
        assert message == realMessage, "Message should show that the stat rose"
        
    def degree2(self):
        """ test message with satt mod change of 2 """
        delegate = self.buildStatModDelegate(2)
        message = delegate.getMessage()
        realMessage = self.riseOrFall[True] + self.sharply[2]
        assert message == realMessage, "Message should show that the stat rose sharply"
        
    def degreeNeg1(self):
        """ test message with satt mod change of -1 """
        delegate = self.buildStatModDelegate(-1)
        message = delegate.getMessage()
        realMessage = self.riseOrFall[False] + self.sharply[1]
        assert message == realMessage, "Message should show that the stat fell"
        
    def degreeNeg2(self):
        """ test message with satt mod change of -2 """
        delegate = self.buildStatModDelegate(-2)
        message = delegate.getMessage()
        realMessage = self.riseOrFall[False] + self.sharply[2]
        assert message == realMessage, "Message should show that the stat fell sharply"
        
testcasesGetMessage = ["degree1", "degree2", "degreeNeg1", "degreeNeg2"]
suiteGetMessage = unittest.TestSuite(map(getMessage, testcasesGetMessage))

##########################################################

class applyEffect(unittest.TestCase):
    """ Tests that the stat modifiers are changed correctly """
    
    def setUp(self):
        """ Builds the BattleSide """
        self.stat = "ATK"
        self.pkmn = BuildPokemonBattleWrapper()
        
    def buildStatModDelegate(self, degree):
        """ Returns a stat mod delegate with the given degree """
        return StatModDelegate(self.stat, degree, 1)
        
    def modIncrease(self):
        """ test that modifiers can increase """
        delegate = self.buildStatModDelegate(1)
        message = delegate.applyEffect(self.pkmn, self.pkmn, None)
        assert self.pkmn.statMods[self.stat] == 1, "ATK should be 1"
        
    def modDecrease(self):
        """ test that modifiers can decrease """
        delegate = self.buildStatModDelegate(-1)
        message = delegate.applyEffect(self.pkmn, self.pkmn, None)
        assert self.pkmn.statMods[self.stat] == -1, "ATK should be -1"
        
    def modStack(self):
        """ test that modifiers stack on the preceding value """
        self.pkmn.statMods[self.stat] = 1
        delegate = self.buildStatModDelegate(-2)
        message = delegate.applyEffect(self.pkmn, self.pkmn, None)
        assert self.pkmn.statMods[self.stat] == -1, "ATK should be -1"
        
    def modTooHigh(self):
        """ test that modifiers stack on the preceding value """
        self.pkmn.statMods[self.stat] = 6
        delegate = self.buildStatModDelegate(2)
        message = delegate.applyEffect(self.pkmn, self.pkmn, None)[0]
        
        assert self.pkmn.statMods[self.stat] == 6, "ATK should be 6"
        find = message.find(StatModDelegate.noChangeUp)
        assert not find == -1,"Should contain the message for going too high"
        
    def modTooLow(self):
        """ test that modifiers stack on the preceding value """
        self.pkmn.statMods[self.stat] = -6
        delegate = self.buildStatModDelegate(-2)
        message = delegate.applyEffect(self.pkmn, self.pkmn, None)[0]
        
        assert self.pkmn.statMods[self.stat] == -6, "ATK should be -6"
        find = message.find(StatModDelegate.noChangeDown)
        assert not find == -1, "Should contain the message for going too low"
        

testcasesApplyEffect = ["modIncrease", "modDecrease", "modStack",  
                                   "modTooHigh", "modTooLow"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect)) 
 
#########################################################

class getHeader(unittest.TestCase):
    """ Test that get Header returns the correct header """
    
    def setUp(self):
        """ Builds the BattleSide """
        self.stat = "ATK"
        self.pkmn = BuildPokemonBattleWrapper()
        
    def buildStatModDelegate(self, degree):
        """ Returns a stat mod delegate with the given degree """
        return StatModDelegate(self.stat, degree, 1)
        
    def testHeader(self):
        """ Test that the get Header returns the correct header """
        delegate = self.buildStatModDelegate(1)
        header = delegate.getHeader(self.pkmn)
        find = header.find("{0}'s {1}".format(self.pkmn.pkmn.name, self.stat))
        assert not find == -1, "Should have the format name's stat"
        
testcasesGetHeader = ["testHeader"]
suiteGetHeader = unittest.TestSuite(map(getHeader, testcasesGetHeader)) 

#########################################################
 
suites = [suiteCheckNoChange, suiteGetMessage, suiteApplyEffect, suiteGetHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()