from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.attack import Attack
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

from Pokemon.pokemon import Pokemon

import unittest

class coreDamage(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.battlePkmn = BuildPokemonBattleWrapper()
        self.pkmn = self.battlePkmn.pkmn
        
        self.delegate = DamageDelegate(None, 50, 1)
        self.pkmn.battleDelegate.stats["ATK"] = 10
        self.pkmn.battleDelegate.stats["DEF"] = 10
        self.pkmn.battleDelegate.level = 5
        
        self.core = self.delegate.coreDamage(self.battlePkmn, self.battlePkmn) - 2
        
    def testAtkEffect(self):
        """ Test that altering ATK has the correct effect """
        self.pkmn.battleDelegate.stats["ATK"] = self.pkmn.battleDelegate.stats["ATK"]*2
        damage = self.delegate.coreDamage(self.battlePkmn, self.battlePkmn) - 2
        
        assert damage == 2*self.core, "Damage should double when Attack is doubled"
        
    def testDefEffect(self):
        """ Test that altering DEF has the correct effect """
        self.pkmn.battleDelegate.stats["DEF"] = self.pkmn.battleDelegate.stats["DEF"]*2
        damage = self.delegate.coreDamage(self.battlePkmn, self.battlePkmn) - 2
        
        assert damage == self.core/2.0, "Damage should half when Defense is doubled"
        
    def testPowerEffect(self):
        """ Test that altering Power has the correct effect """
        self.delegate.power = 100
        damage = self.delegate.coreDamage(self.battlePkmn, self.battlePkmn) - 2
        
        assert damage == self.core*2.0, "Damage should double when Power is doubled"

# Collect all test cases in this class      
testcasesCoreDamage = ["testAtkEffect", "testDefEffect", "testPowerEffect"]
suiteCoreDamage = unittest.TestSuite(map(coreDamage, testcasesCoreDamage))

#########################################################


class atkAndDefType(unittest.TestCase):
    """ Test that the damage delegate can correctly choose if it should use physical 
    ATK and DEF or special SATK and SDEF """
    
    def physical(self):
        """ Test that it returns correctly for physical attacks """
        delegate = DamageDelegate(None, None, 1)
        atkStat, defStat = delegate.getAtkAndDefType()
        assert atkStat == "ATK", "Attack stat should be physical"
        assert defStat == "DEF", "Defense stat should be physical"
        
    def special(self):
        """ Test that it returns correctly for physical attacks """
        delegate = DamageDelegate(None, None, 0)
        atkStat, defStat = delegate.getAtkAndDefType()
        assert atkStat == "SATK", "Attack stat should be special"
        assert defStat == "SDEF", "Defense stat should be special"

# Collect all test cases in this class      
testcasesAtkAndDefType = ["physical", "special"]
suiteAtkAndDefType = unittest.TestSuite(map(atkAndDefType, testcasesAtkAndDefType))

#########################################################

class getStatWithMod(unittest.TestCase):
    """ Test that get Stat with Mod, modifies the satats correctly """
    
    def setUp(self):
        """ Build the Pkmn """
        self.stat = "ATK"
        self.battlePkmn = BuildPokemonBattleWrapper()
        self.pkmn = self.battlePkmn.pkmn
    
    def buildDamageDelegate(self):
        """ Returns a Damage Delegate """
        return DamageDelegate(None, 50, 1)
        
    def noModifier(self):
        """ Test that no modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        pokeValue = self.pkmn.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.battlePkmn)
        assert pokeValue == sideValue, "Stat should be unchanged"
        
    def highModifier(self):
        """ Test that high modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        self.battlePkmn.statMods[self.stat] = 2
        pokeValue = self.pkmn.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.battlePkmn)
        
        assert pokeValue*2.0 == sideValue, "Stat should be twice normal"
        
    def lowModifier(self):
        """ Test that low modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        self.battlePkmn.statMods[self.stat] = -2
        pokeValue = self.pkmn.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.battlePkmn)
        
        assert pokeValue/2.0 == sideValue, "Stat should be half normal"

# Collect all test cases in this class      
testcasesGetStatWithMod = ["noModifier", "highModifier", "lowModifier"]
suiteGetStatWithMod = unittest.TestSuite(map(getStatWithMod, testcasesGetStatWithMod))
        
#########################################################

class normalize(unittest.TestCase):
    """ Tests that Normalize normalizes correctly """
    
    def setUp(self):
        """ Build the Damage Delegate """
        self.delegate = DamageDelegate(None, 0, 1)
        
    def zero(self):
        """ Test that 0 is normalized correctly """
        damage = 0
        newDamage = self.delegate.normalize(damage)
        assert newDamage == 0, "Should return zero"
        
    def lessThanOne(self):
        """ Test that < 1 is normalized correctly """
        damage = 0.1
        newDamage = self.delegate.normalize(damage)
        assert newDamage == 1, "Should return one if between 0 and 1"
        
    def normalizeInt(self):
        """ Test that normalizing an int returns the int """
        damage = 3
        newDamage = self.delegate.normalize(damage)
        assert newDamage == damage, "Should return the number if its an int"
        
    def normalizeFloat(self):
        """ Test that normalizing a float returns the int """
        damage = 3.3
        newDamage = self.delegate.normalize(damage)
        assert newDamage == int(damage), "Should return the floored number if its an int"

# Collect all test cases in this class      
testcasesNormalize = ["zero", "lessThanOne", "normalizeInt", "normalizeFloat"]
suiteNormalize  = unittest.TestSuite(map(normalize , testcasesNormalize ))
        
#########################################################

class getStab(unittest.TestCase):
    """ Tests that STAB returns the appropriate modifier """
    
    def setUp(self):
        """ Build the Attack and Damage Delegate """
        attack = Attack()
        attack.type ="FIRE"
        self.delegate = DamageDelegate(attack, 0, 1)
        
    def hasStab(self):
        """ Test that it correctly returns STAB modifier """
        pkmn = BuildPokemonBattleWrapper("CHARMANDER")
        stab = self.delegate.getStab(pkmn)
        assert stab == 1.5, "Should return with STAB modifier"
        
    def noStab(self):
        """ Test that it correctly returns STAB modifier """
        pkmn = BuildPokemonBattleWrapper("BULBASAUR")
        stab = self.delegate.getStab(pkmn)
        assert stab == 1, "Should return with modifier of 1"

# Collect all test cases in this class      
testcasesGetStab = ["hasStab", "noStab"]
suiteGetStab  = unittest.TestSuite(map(getStab , testcasesGetStab ))
        
#########################################################
 
suites = [suiteCoreDamage, suiteAtkAndDefType, suiteGetStatWithMod, suiteNormalize, suiteGetStab]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()