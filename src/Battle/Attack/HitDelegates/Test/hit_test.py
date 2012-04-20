import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildAttack

from Battle.Attack.HitDelegates.hit_delegate import HitDelegate
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

class hit(unittest.TestCase):
    """ Test cases of hit """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.attack = BuildAttack()
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.toHit = 100.0
        self.delegate = HitDelegate(self.attack, self.toHit)
        
    def fainted(self):
        """ Test that if the target is fainted the attack misses """
        self.target.faint()
        hit, message = self.delegate.hit(self.user, self.target)
        assert not hit, "Should miss if the target is fainted"
        
    def dodging(self):
        """ Test that if the target is dodging the attack misses """
        self.target.dodge = "DIG"
        hit, message = self.delegate.hit(self.user, self.target)
        assert not hit, "Should miss if the target is dodging"
        
    def otherwise(self):
        """ Test that the attack hits if the target is not dodging or fainted """
        hit, message = self.delegate.hit(self.user, self.target)
        assert hit, "Should hit otherwise"

# Collect all test cases in this class
testcasesHit = ["fainted", "dodging", "otherwise"]
suiteHit = unittest.TestSuite(map(hit, testcasesHit))

##########################################################

class getChanceToHit(unittest.TestCase):
    """ Test cases of getChanceToHit """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.toHit = 100.0
        self.delegate = HitDelegate(None, self.toHit)
        
    def accuracyMods(self):
        """ Test that accuracy mods correctly change the accuracy """
        length = len(HitDelegate.accMods)/2
        for i in range(-length, length+1):
            self.user.statMods["ACC"] = i
            
            chance = self.delegate.getChanceToHit(self.user, self.target)
            assert chance == self.toHit*HitDelegate.accMods[i], "Chance should be accuracy modded by acc mod"
        
    def evasionMods(self):
        """ Test that evasion mods correctly change the accuracy """
        length = len(HitDelegate.accMods)/2
        for i in range(-1*length, length+1):
            self.target.statMods["EVAS"] = i
            
            chance = self.delegate.getChanceToHit(self.user, self.target)
            assert chance == self.toHit*HitDelegate.accMods[-i], "Chance should be accuracy modded by evas mod"
            
    def balanced(self):
        """ Test that evasion and accuracy mods balance each other out """
        length = len(HitDelegate.accMods)/2
        for i in range(-1*length, length+1):
            self.user.statMods["ACC"] = i
            self.target.statMods["EVAS"] = i
            
            chance = self.delegate.getChanceToHit(self.user, self.target)
            assert chance == self.toHit, "Chance should be accuracy when evas and acc are the same"

# Collect all test cases in this class
testcasesGetChanceToHit = ["accuracyMods", "evasionMods", "balanced"]
suiteGetChanceToHit = unittest.TestSuite(map(getChanceToHit, testcasesGetChanceToHit))

##########################################################

class getMod(unittest.TestCase):
    """ Test cases of getMod """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.delegate = HitDelegate(None, 100)
        
    def accuracyMods(self):
        """ Test that accuracy mods correctly change the accuracy """
        length = len(HitDelegate.accMods)/2
        for i in range(-length, length+1):
            self.user.statMods["ACC"] = i
            
            mod = self.delegate.getMod(self.user, self.target)
            assert mod == HitDelegate.accMods[i], "Mod should be acc mod"
        
    def evasionMods(self):
        """ Test that evasion mods correctly change the accuracy """
        length = len(HitDelegate.accMods)/2
        for i in range(-1*length, length+1):
            self.target.statMods["EVAS"] = i
            
            mod = self.delegate.getMod(self.user, self.target)
            assert mod == HitDelegate.accMods[-i], "Mod should be evas mod"
            
    def balanced(self):
        """ Test that evasion and accuracy mods balance each other out """
        length = len(HitDelegate.accMods)/2
        for i in range(-1*length, length+1):
            self.user.statMods["ACC"] = i
            self.target.statMods["EVAS"] = i
            
            mod = self.delegate.getMod(self.user, self.target)
            assert mod == HitDelegate.accMods[0], "Mod should be 1 when evas and acc are the same"

# Collect all test cases in this class
testcasesGetMod = ["accuracyMods", "evasionMods", "balanced"]
suiteGetMod = unittest.TestSuite(map(getMod, testcasesGetMod))

##########################################################

class checkHit(unittest.TestCase):
    """ Test cases of checkHit """
    
    def  setUp(self):
        """ Build the Delegate for the test """
        self.delegate = HitDelegate(None, 100)
        
    def noHit(self):
        """ Test that it does not hit if the toHit is lower than the Rand """
        rand = 100
        toHit = 0
        
        hit = self.delegate.checkHit(rand, toHit)
        assert not hit, "Should not hit"
        
    def hit(self):
        """ Test that it hits if toHit is greater than the Rand """
        rand = 0
        toHit = 100
        
        hit = self.delegate.checkHit(rand, toHit)
        assert hit, "Should hit"

# Collect all test cases in this class
testcasesCheckHit = ["noHit", "hit"]
suiteCheckHit = unittest.TestSuite(map(checkHit, testcasesCheckHit))

##########################################################

class dodging(unittest.TestCase):
    """ Test that dodging returns the correct values """
    
    def setUp(self):
        """ Build Pkmn and Delegate for use in test cases """
        self.pkmn =  BuildPokemonBattleWrapper()
        self.delegate = HitDelegate(None, 100)
    
    def dodging(self):
        """ Test dodging function returns true correctly when the opp is dodging """
        self.pkmn.dodge = "DIG"
        assert self.delegate.dodging(self.pkmn), "Should be dodging"
        
    def notDodging(self):
        """ Test dodging function returns false when the opp is not dodging """
        self.pkmn.dodge = None
        assert not  self.delegate.dodging(self.pkmn), "Should not be dodging"
        
testcasesDodging= ["dodging", "notDodging"]
suiteDodging= unittest.TestSuite(map(dodging, testcasesDodging))

#########################################################

class hitGhost(unittest.TestCase):
    """ Test that hitGhost returns the correct values """
    
    def setUp(self):
        """ Build Pkmn and Delegate for use in test cases """
        self.attack = BuildAttack()
        self.pkmn =  BuildPokemonBattleWrapper()
        self.delegate = HitDelegate(self.attack, 100)
        
        self.damage = self.attack.damageDelegate
        
    def cantHit(self):
        """ Test hitGhost function returns false when the opp is a Ghost and a FIGHTING or NORMAL attack is used """
        self.pkmn.setTypes(["GHOST"])
        
        self.attack.type = "NORMAL"
        assert not  self.delegate.hitGhost(self.pkmn), "Should not be able to hit a Ghost with a Normal Attack"
        
        self.attack.type = "FIGHTING"
        assert not  self.delegate.hitGhost(self.pkmn), "Should not be able to hit a Ghost with a Fighting Attack"
        
    def status(self):
        """ Test hitGhost function returns true correctly when the attack is a status attack """
        self.attack.damageDelegate = NullDamageDelegate()
        self.pkmn.setTypes(["GHOST"])
        self.attack.type = "NORMAL"
        assert self.delegate.hitGhost(self.pkmn), "Should hit a Ghost if it is a status move"
        
    def notGhost(self):
        """ Test hitGhost function returns true when the opp is not a Ghost Type """
        self.pkmn.setTypes(["NORMAL"])
        assert self.delegate.hitGhost(self.pkmn), "Should be able to hit a Normal Type Pkmn"
        
    def notFightingOrNormal(self):
        """ Test hitGhost function returns true when the opp is a Ghost but not hit with a type that should miss """
        self.pkmn.setTypes(["GHOST"])
        
        self.attack.type = "FIRE"
        assert self.delegate.hitGhost(self.pkmn), "Should be able to hit a Ghost with any attack that isn't Normal or Fighting Attack"
        
testcasesHitGhost= ["cantHit", "status", "notGhost", "notFightingOrNormal"]
suiteHitGhost= unittest.TestSuite(map(hitGhost, testcasesHitGhost))

#########################################################
 
suites = [suiteHit, suiteGetChanceToHit, suiteGetMod, suiteCheckHit, suiteDodging, suiteHitGhost]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()