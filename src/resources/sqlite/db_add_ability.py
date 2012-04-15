import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder
from resources.sqlite.db_add_effect import DBAddEffect

class DBAddAbility(DBAdder):
    """ Adds an ability to the Database """
    def __init__(self):
        """  """
        self.delegateType = "Ability"
        self.commands = {'p':self.addParameters, 
                                   'a':self.addAbilityType}
        self.vals = {'name':None, 
                          'ability_type_id':None,
                          'ability_id':None,
                          'effects':[]}
                          
        self.getIDForType = {'ACC MOD':self.buildAccMod,
                                       'BOOST STAB':self.buildAbilityWithNone,
                                       'CANT LOWER STAT':self.buildCantLowerStat,
                                       'EFFECT AFTER TURN':self.buildAbilityWithEffects,
                                       'EFFECT ON CRIT':self.buildAbilityWithEffects,
                                       'EFFECT ON STAT MOD':self.buildAbilityWithEffects,
                                       'NO CRIT':self.buildAbilityWithNone,
                                       'SKIP TURN':self.buildAbilityWithNone,
                                       'SNIPER':self.buildAbilityWithNone,
                                       'STAT MOD ON STATUS':self.buildStatModOnStatus}
        
        
        self.connection = PkmnDBConnect()
        self.cursor = self.connection.cursor()
    
    def execute(self, params, close = True):
        """  """
        for param in params:
            cmd = param[0]
            cmdParams = param[2:].split(':')
            
            self.commands[cmd](cmdParams)
            
        self.addAbility()
            
        self.connection.commit()
        
        if (close):
            self.connection.close()
        
    def addAbility(self):
        """ Adds the attack to the database """
        params = []
        toAdd = []
        
        for key in self.vals.keys():
            if self.vals[key] is None:
                continue
                
            if key == 'effects':
                continue   
                
            params += [key]
            toAdd += [self.vals[key]]
            
        paramStr = self.GetStrFromList(params)
        
        print "Adding Ability:", self.vals['name']
        self.insertIntoDB("Ability", paramStr, toAdd)
        
        self.cursor.execute("SELECT id from Ability where name = ?", (self.vals['name'],))
        id = self.cursor.fetchone()[0]
        
        self.connectToExtraEffects(id)
            
    def addParameters(self, vals):
        """ Adds Attack specific parameters """
        self.vals['name'] = vals[0]
        print "Building Ability:", self.vals['name']
        self.checkForAbilityAlready()
        
    def addAbilityType(self, vals):
        """  """
        type = vals[0].strip()
        self.cursor.execute("SELECT id FROM AbilityVariants where type = ?", (type,))
        val = self.cursor.fetchone()
        if val is None:
            print "%s ability variant does not exist" % type
            raise Exception()
        
        self.vals['ability_type_id'] = val[0]
        self.vals['ability_id'] = self.getIDForType[type](type, vals[1:])
        
        
    def buildAbilityWithEffects(self, type, vals):
        """  """
        table = "AbilityEffectsJoin"
        effects = vals[0].split('_')[1:]
        
        for effect in effects:
            effectAdder = DBAddEffect(self.connection, self.cursor)
            effect_type_id, effect_id = effectAdder.execute(effect[2:].split('%'))
            self.vals['effects'].append((effect_type_id, effect_id,))
        
    def buildAbilityWithNone(self, type, vals):
        """  """
        return None
        
    def buildAccMod(self, type, vals):
        """  """
        table = "AccModAbility"
        mod = float(vals[0])
        
        toAdd = (mod,)
        where = "mod = ?"
        params = "mod"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildCantLowerStat(self, type, vals):
        """  """
        table = "CantLowerStatAbility"
        stat = vals[0]
        
        toAdd = (stat,)
        where = "stat = ?"
        params = "stat"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildStatModOnStatus(self, type, vals):
        """  """
        table = "StatModOnStatusAbility"
        status = vals[0]
        stat = vals[1]
        mod = float(vals[2])
        
        toAdd = (status, stat, mod,)
        where = "status = ? and stat = ? and mod = ?"
        params = "status, stat, mod"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def checkForAbilityAlready(self):
        """  """
        self.cursor.execute("SELECT id from Ability where name = ?", (self.vals['name'],))
        t = self.cursor.fetchone()
        
        if not t is None:
            print "Ability %s already exists" % self.vals['name']
            raise Exception()
            
    def connectToExtraEffects(self, id):
        """  """
        table = "AbilityEffectsJoin"
        paramStr = "ability_id, effect_type_id, effect_id"
        
        for effect in self.vals['effects']:
            self.insertIntoDB(table, paramStr, (id,)+effect)