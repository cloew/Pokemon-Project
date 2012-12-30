import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.damagescale_delegate import DamageScaleDelegate

class coreDamage(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    
    def setUp(self):
        """ Build the Pkmn and Delegates for use in the tests """
        power = 50
        isPhysical = 1
        self.delegate = DamageScaleDelegate(None, power, isPhysical, 2, 5)
        self.standardDelegate = DamageDelegate(None, power, isPhysical)
        
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
    def damageIsSameOnFirstTurn(self):
        """ Test that damage is equivalent before the scale kicks in """
        self.delegate.turnsToGo = 0
        standardDamage = self.standardDelegate.coreDamage(self.user, self.target)
        damage = self.delegate.coreDamage(self.user, self.target)
        assert standardDamage == damage, "Should be no difference in damage on first turn"
        
    def damageIsScaled(self):
        """ Test that the damage is scaled when there is a scale """
        self.delegate.turnsToGo = 2
        scale = self.delegate.getScale()
        
        standardDamage = self.standardDelegate.coreDamage(self.user, self.target)
        damage = self.delegate.coreDamage(self.user, self.target)
        
        assert (standardDamage-2)*scale+2 == damage, "Damage should be scaled by the scale factor"

# Collect all test cases in this class      
testcasesCoreDamage = ["damageIsSameOnFirstTurn", "damageIsScaled"]
suiteCoreDamage = unittest.TestSuite(map(coreDamage, testcasesCoreDamage))

#########################################################

class getScale(unittest.TestCase):
    """ Test that getScale returns correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.factor = 2
        self.delegate = DamageScaleDelegate(None, 50, 1, self.factor, 5)
        
    def correctScale(self):
        """ Test that getScale returns the correct scale """
        self.delegate.turnOn = 0
        scale = self.delegate.getScale()
        assert scale == 1, "Scale should be 1 when turnsToGo is 0"
        
    def correctScaleAfterInc(self):
        """ Test that scale returns correctly after the turn increments """
        self.delegate.turnOn = 0
        scale = self.delegate.getScale()
        
        self.delegate.incTurns()
        scale2 = self.delegate.getScale()
        
        assert scale == scale2/self.factor, "Scale should be half of the scale when turnsToGo is 0"

# Collect all test cases in this class      
testcasesGetScale = ["correctScale", "correctScaleAfterInc"]
suiteGetScale = unittest.TestSuite(map(getScale, testcasesGetScale))

#########################################################

class applyEffect(unittest.TestCase):
    """ Test that applyEffect returns correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = DamageScaleDelegate(None, 50, 1, 1, 5)
        
    def turnZero(self):
        """ Test that applyEffect operates correctly on turn 0 """
        self.delegate.turnOn = 0
        self.pkmn.actionLock = None
        self.delegate.applyEffect(self.pkmn, None, None)
        
        assert self.pkmn.actionLock is not None, "Should have an action Lock"
        assert self.delegate.turnOn == 1, "Turns should be incremented"
        
    def otherwise(self):
        """ Test that applyEffect does not do anything except increment turns if the turn is not zero """
        self.delegate.turnOn = 1
        self.pkmn.actionLock = None
        self.delegate.applyEffect(self.pkmn, None, None)
        
        assert self.pkmn.actionLock is None, "Should not have an actionLock"
        assert self.delegate.turnOn == 2, "Turns should be incremented"

# Collect all test cases in this class      
testcasesApplyEffect = ["turnZero", "otherwise"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

#########################################################

suites = [suiteCoreDamage, suiteGetScale, suiteApplyEffect]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()