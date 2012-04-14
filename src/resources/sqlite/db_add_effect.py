import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddEffect(DBAdder):
    """  """
    delegateType = "Effect"
    variantTable = "EffectDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'APPLY LOCK':self.buildApplyLock,
                                       'CHANCE':self.buildChance,
                                       'CHARGE':self.buildCharge,
                                       'CONFUSE':self.buildConfuse,
                                       'CRIT MOD':self.buildCritMod,
                                       'CURE STATUS':self.buildCureStatus,
                                       'DAMAGE IS EFFECT':self.buildDamageIsEffect,
                                       'DIVERGE ON FAINT':self.buildDivergeOnFaint,
                                       'DODGE':self.buildDodge,
                                       'FLINCH':self.buildFlinch,
                                       'HEAL DAMAGE RATIO':self.buildHealDamageRatio,
                                       'HEAL HP RATIO':self.buildHealHPRatio,
                                       'LEECH':self.buildLeech,
                                       'MULTI TUNR RANGE':self.buildMultiTurnRange,
                                       'RND STAT MOD':self.buildRndStatMod,
                                       'RECOIL':self.buildRecoil
                                       'RESET STAT MODS':self.buildResetStatMods,
                                       'RANDOM SWITCH':self.buildRandomSwitch,
                                       'PERIODIC HEAL':self.buildPeriodicHeal,
                                       'SELFDESTRUCT':self.buildSelfdestruct,
                                       'STAT MOD':self.buildStatMod,
                                       'STATUS':self.buildStatus,
                                       'SWAP ABILITY':self.buildSwapAbility,
                                       'SWAP STATS':self.buildSwapStats,
                                       'SWAP STAT MODS':self.buildSwapStatMods,
                                       'SWITCH':self.buildSwitch,
                                       'TRAP':self.buildTrap,
                                       'USELESS':self.buildUseless}
        
    def buildApplyLock(self, params):
        """  """
        type = "APPLY LOCK"
        table = "ApplyLockEffect"
        turns = int(params[0])
        affectUser = int(params[1])
        where = "turns = ? and affectUser = ?"
        toAdd = (turns, affectUser,)
        params = "turns, affectUser"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildChance(self, params):
        """  """
        type = "CHANCE"
        table = "ChanceEffect"
        chance = int(params[0])
        where = "chance = ?"
        toAdd = (chance,)
        paramStr = "chance"
        
        id = self.buildDelegate(type, table, where, toAdd, paramStr)
        
        self.addEffects(id, params[1])
        
        return id
        
    def buildCharge(self, params):
        """  """
        type = "CHARGE"
        table = "ChargeEffect"
        turns = int(params[0])
        hitOnTurn = int(params[1])
        message = params[2]
        where = "turns = ? and hitOnTurn = ? and message = ?"
        toAdd = (turns, hitOnTurn, message,)
        params = "turns, hitOnTurn, message"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildConfuse(self, params):
        """  """
        type = "CONFUSE"
        table = "ConfuseEffect"
        affectUser = int(params[0])
        where = "affectUser = ?"
        toAdd = (affectUser,)
        params = "affectUser"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildCritMod(self, params):
        """  """
        type = "CRIT MOD"
        table = "CritModEffect"
        degree = int(params[0])
        where = "degree = ?"
        toAdd = (degree,)
        params = "degree"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildCureStatus(self, params):
        """  """
        type = "CURE STATUS"
        table = "CureStatusEffect"
        status = params[0]
        affectUser = int(params[1])
        where = "status = ? and degree = ?"
        toAdd = (status, degree,)
        params = "status, degree"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildDamageIsEffect(self, params):
        """  """
        return None
        
    def buildDivergeOnFaint(self, params):
        """  """
        type = "DIVERGE ON FAINT"
        table = "DivergeEffect"
        where = "diverge_owner_id = ? and normal_owner_id = ?"
        toAdd = (0,0)
        params = "diverge_owner_id, normal_owner_id"
        
        id = self.buildDelegate(type, table, where, toAdd, params)
        self.cursor.execute("UPDATE %s set diverge_owner_id=?, normal_owner_id=? where id = ?" % table, (id, -id, id))
        
        self.addEffects(id, params[0])
        self.addEffects(-id, params[1])
        
        return id
        
    def buildDodge(self, params):
        """  """
        type = "DODGE"
        table = "DodgeEffect"
        dodge = params[0]
        message = params[1]
        where = "dodge = ? and message = ?"
        toAdd = (dodge, degree,)
        params = "dodge, message"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildFlinch(self, params):
        """  """
        return None
        
    def buildHealDamageRatio(self, params):
        """  """
        type = "HEAL DAMAGE RATIO"
        table = "HealByRatioEffect"
        ratio = int(params[0])
        where = "ratio = ?"
        toAdd = (ratio,)
        params = "ratio"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildHealHPRatio(self, params):
        """  """
        type = "HEAL HP RATIO"
        table = "HealByRatioEffect"
        ratio = int(params[0])
        where = "ratio = ?"
        toAdd = (ratio,)
        params = "ratio"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildLeech(self, params):
        """  """
        type = "LEECH"
        table = "LeechEffect"
        start = params[0]
        message = params[1]
        where = "start = ? and message = ?"
        toAdd = (start, message,)
        params = "start, message"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildMultiTurnRange(self, params):
        """  """
        type = "MULTI TURN RANGE"
        table = "MultiTurnRangeEffect"
        min = int(params[0])
        max = int(params[1])
        where = "min = ? and max = ?"
        toAdd = (min, max,)
        paramStr = "min, max"
        
        id = self.buildDelegate(type, table, where, toAdd, paramStr)
        self.addEffects(id, params[2])
        
        return id
        
    def buildRndStatMod(self, params):
        """  """
        type = "RND STAT MOD"
        table = "RandomStatModEffect"
        degree = int(params[0])
        affectUser = int(params[1])
        where = "degree = ? and affectUser = ?"
        toAdd = (degree, affectUser,)
        params = "degree, affectUser"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildRecoil(self, params):
        """  """
        type = "RECOIL"
        table = "RecoilEffect"
        ratio = int(params[0])
        where = "ratio = ?"
        toAdd = (ratio,)
        params = "ratio"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildResetStatMods(self, params):
        """  """
        return None
        
    def buildRandomSwitch(self, params):
        """  """
        type = "RANDOM SWITCH"
        table = "SwitchEffect"
        affectUser = int(params[0])
        reset = int(params[1])
        where = "affectUser = ? and reset = ?"
        toAdd = (affectUser, reset,)
        params = "affectUser, reset"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildPeriodicHeal(self, params):
        """  """
        type = "PERIODIC HEAL"
        table = "PeriodicHealEffect"
        start = params[0]
        message = params[1]
        where = "start = ? and message = ?"
        toAdd = (start, message,)
        params = "start, message"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildSelfdestruct(self, params):
        """  """
        return None
        
    def buildStatMod(self, params):
        """  """
        type = "STAT MOD"
        table = "StatModEffect"
        stat = params[0]
        degree = int(params[1])
        affectUser = int(params[2])
        where = "stat = ? and degree = ? and affectUser = ?"
        toAdd = (stat, degree, affectUser,)
        params = "stat, degree, affectUser"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildStatus(self, params):
        """  """
        type = "STATUS"
        table = "StatusEffect"
        status = params[0]
        affectUser = int(params[1])
        where = "status = ? and affectUser = ?"
        toAdd = (status, affectUser,)
        params = "status, affectUser"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildSwapAbility(self, params):
        """  """
        return None
        
    def buildSwapStats(self, params):
        """  """
        type = "SWAP STATS"
        table = "SwapStatsEffect"
        stat1 = params[0]
        stat2 = int(params[1])
        where = "stat1 = ? and stat2 = ?"
        toAdd = (stat1, stat2,)
        params = "stat1, stat2"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildSwapStatMods(self, params):
        """  """
        return None
        
    def buildTrap(self, params):
        """  """
        type = "TRAP"
        table = "TrapEffect"
        start = params[0]
        message = params[1]
        done = params[2]
        where = "start = ? and message = ? and done = ?"
        toAdd = (start, message, done)
        params = "start, message, done"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildUseless(self, params):
        """  """
        return None
        
    def addEffects(self, id, paramStr):
        """  """
        effects = paramStr.split('_')
        table = "EffectEffectJoin"
        params = "owner_id, owner_type_id, effect_id, effect_type_id"
        
        for effect in effects:
            effect_type_id, effect_id = self.execute(effect[2:].split('%'))
            self.insertIntoDB(table, params, (id, self.type_id, effect_id, effect_type_id,))
            