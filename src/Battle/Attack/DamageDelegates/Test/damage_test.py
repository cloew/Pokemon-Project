from Battle.Attack.attack import Attack
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class coreDamage(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        trainer = Trainer()
        self.pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [self.pokemon]
        self.side = BattleSide(trainer)
        self.delegate = DamageDelegate(None, 50, 1)
        self.pokemon.battleDelegate.stats["ATK"] = 10
        self.pokemon.battleDelegate.stats["DEF"] = 10
        self.pokemon.battleDelegate.level = 5
        
        self.core = self.delegate.coreDamage(self.side, self.side) - 2
        
    def testAtkEffect(self):
        """ Test that altering ATK has the correct effect """
        self.pokemon.battleDelegate.stats["ATK"] = self.pokemon.battleDelegate.stats["ATK"]*2
        damage = self.delegate.coreDamage(self.side, self.side) - 2
        
        assert damage == 2*self.core, "Damage should double when Attack is doubled"
        
    def testDefEffect(self):
        """ Test that altering ATK has the correct effect """
        self.pokemon.battleDelegate.stats["DEF"] = self.pokemon.battleDelegate.stats["DEF"]*2
        damage = self.delegate.coreDamage(self.side, self.side) - 2
        
        assert damage == self.core/2.0, "Damage should half when Defense is doubled"
        
    def testPowerEffect(self):
        """ Test that altering ATK has the correct effect """
        self.delegate.power = 100
        damage = self.delegate.coreDamage(self.side, self.side) - 2
        
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
        """ Build the side """
        self.stat = "ATK"
        trainer = Trainer()
        self.pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [self.pokemon]
        self.side = BattleSide(trainer)
        
    
    def buildDamageDelegate(self):
        """ Returns a damage delegate """
        return DamageDelegate(None, 50, 1)
        
    def noModifier(self):
        """ Test that no modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        pokeValue = self.pokemon.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.side)
        assert pokeValue == sideValue, "Stat should be unchanged"
        
    def highModifier(self):
        """ Test that high modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        self.side.statMods[self.stat] = 2
        pokeValue = self.pokemon.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.side)
        
        assert pokeValue*2.0 == sideValue, "Stat should be twice normal"
        
    def lowModifier(self):
        """ Test that low modifier returns the correct value """
        delegate = self.buildDamageDelegate()
        self.side.statMods[self.stat] = -2
        pokeValue = self.pokemon.battleDelegate.stats[self.stat]
        sideValue = delegate.getStatWithMod(self.stat, self.side)
        
        assert pokeValue/2.0 == sideValue, "Stat should be half normal"

# Collect all test cases in this class      
testcasesGetStatWithMod = ["noModifier", "highModifier", "lowModifier"]
suiteGetStatWithMod = unittest.TestSuite(map(getStatWithMod, testcasesGetStatWithMod))
        
#########################################################

class getStab(unittest.TestCase):
    """ Tests that STAB returns the appropriate modifier """
    
    def setUp(self):
        """ Build the Attack """
        attack = Attack()
        attack.type ="FIRE"
        self.delegate = DamageDelegate(attack, 0, 1)
        
    def hasStab(self):
        """ Test that it correctly returns STAB modifier """
        poke = Pokemon("CHARMANDER")
        stab = self.delegate.getStab(poke)
        assert stab == 1.5, "Should return with STAB modifier"
        
    def noStab(self):
        """ Test that it correctly returns STAB modifier """
        poke = Pokemon("BULBASAUR")
        stab = self.delegate.getStab(poke)
        assert stab == 1, "Should return with modifier of 1"

# Collect all test cases in this class      
testcasesGetStab = ["hasStab", "noStab"]
suiteGetStab  = unittest.TestSuite(map(getStab , testcasesGetStab ))
        
#########################################################
 
suites = [suiteCoreDamage, suiteAtkAndDefType, suiteGetStatWithMod, suiteGetStab]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()