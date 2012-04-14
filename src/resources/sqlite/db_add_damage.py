import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddDamage(DBAdder):
    """  """
    delegateType = "Damage"
    variantTable = "DamageDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'BOOST STATUS':self.buildBoostOnStatus,
                                       'CORE':self.buildCore,
                                       'EFFECT ON DAMAGE':self.buildEffectOnDamage,
                                       'FIXED':self.buildFixed,
                                       'HALF HEALTH':self.buildHalfHealth,
                                       'LEVEL':self.buildLevel,
                                       'NO FAINT':self.buildNoFaint,
                                       'ONE HIT KO':self.buildOneHitKO,
                                       'PIERCE DODGE 2X':self.buildPierceDodgeX2,
                                       'SCALE':self.buildScale,
                                       'STAT RATIO FIXED':self.buildStatRatioFixed,
                                       'STAT RATIO RANGE':self.buildStatRatioRange}
     
    def buildBoostOnStatus(self, params):
        """  """
        type = "BOOST ON STATUS"
        table = "BoostOnStatusDamage"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        params = "power, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
     
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreDamageDelegate"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        params = "power, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildEffectOnDamage(self, params):
        """  """
        type = "EFFECT ON DAMAGE"
        table = "CoreDamageDelegate"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        params = "power, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildFixed(self, params):
        """  """
        type = "FIXED"
        table = "FixedDamage"
        damage = int(params[0])
        physical = int(params[1])
        
        toAdd = (damage, physical,)
        where = "damage = ? and physical = ?"
        params = "damage, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildHalfHealth(self, params):
        """  """
        type = "HALF HEALTH"
        table = "HalfHealthDamage"
        physical = int(params[0])
        
        toAdd = (physical,)
        where = "physical = ?"
        params = "physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildLevel(self, params):
        """  """
        type = "LEVEL"
        table = "LevelDamage"
        physical = int(params[0])
        
        toAdd = (physical,)
        where = "physical = ?"
        params = "physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildNoFaint(self, params):
        """  """
        type = "NO FAINT"
        table = "NoFaintDamage"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        params = "power, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildOneHitKO(self, params):
        """  """
        type = "ONE HIT KO"
        table = "OneHitKODamage"
        physical = int(params[0])
        
        toAdd = (power, physical,)
        where = "physical = ?"
        params = "physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildPierceDodgeX2(self, params):
        """  """
        type = "PIERCE DODGE 2X"
        table = "PierceDodge2XDamage"
        power = int(params[0])
        physical = int(params[1])
        pierce = params[2]
        
        toAdd = (power, physical, pierce,)
        where = "power = ? and physical = ? and pierce = ?"
        params = "power, physical, pierce"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildScale(self, params):
        """  """
        type = "SCALE"
        table = "ScaleDamage"
        power = int(params[0])
        physical = int(params[1])
        factor = int(params[2])
        turns = int(params[3])
        
        toAdd = (power, physical, factor, turns,)
        where = "power = ? and physical = ? and factor = ? and turns = ?"
        params = "power, physical, factor, turns"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildStatRatioFixed(self, params):
        """  """
        type = "STAT RATIO FIXED"
        table = "StatRatioDamage"
        physical = int(params[0])
        stat = params[1]
        
        toAdd = (stat, physical,)
        where = "stat = ? and physical = ?"
        params = "stat, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildStatRatioRange(self, params):
        """  """
        type = "STAT RATIO RANGE"
        table = "StatRatioDamage"
        physical = int(params[0])
        stat = params[1]
        
        toAdd = (stat, physical,)
        where = "stat = ? and physical = ?"
        params = "stat, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)