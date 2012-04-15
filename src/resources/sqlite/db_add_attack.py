import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder
from resources.sqlite.db_add_crit import DBAddCrit
from resources.sqlite.db_add_damage import DBAddDamage
from resources.sqlite.db_add_effect import DBAddEffect
from resources.sqlite.db_add_hit import DBAddHit
from resources.sqlite.db_add_speed import DBAddSpeed

class DBAddAttack(DBAdder):
    """ Adds an attack to the Database """
    def __init__(self):
        """  """
        self.commands = {'p':self.addParameters, 'h':self.addHit,
                                   'd':self.addDamage, 'c':self.addCrit, 's':self.addSpeed,
                                   'e':self.addEffect}
        self.vals = {'name':None, 'type_id':None,
                          'hit_type':None, 'hit_id':None,
                          'damage_type':None, 'damage_id':None,
                          'crit_type':None, 'crit_id':None,
                          'speed_type':None, 'speed_id':None,
                          'effects':[]}
        
        
        self.connection = PkmnDBConnect()
        self.cursor = self.connection.cursor()
    
    def execute(self, params, close = True):
        """  """
        for param in params:
            cmd = param[0]
            cmdParams = param[2:].split(':')
            
            self.commands[cmd](cmdParams)
            
        self.addAttack()
            
        self.connection.commit()
        
        if (close):
            self.connection.close()
        
    def addAttack(self):
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
        
        print "Adding Attack:", self.vals['name']
        self.insertIntoDB("Attack", paramStr, toAdd)
        
        self.cursor.execute("SELECT id from Attack where name = ?", (self.vals['name'],))
        id = self.cursor.fetchone()[0]
        
        for effect in self.vals['effects']:
            self.insertIntoDB("AttackEffectsJoin", "attack_id, effect_type, effect_id", (id,)+effect)
            
    def addParameters(self, vals):
        """ Adds Attack specific parameters """
        self.vals['name'] = vals[0]
        type = vals[1].strip()
        print "Building Attack:", self.vals['name']
        self.cursor.execute("SELECT id FROM Type where name = ?", (type,))
        
        val = self.cursor.fetchone()
        if val is None:
            print "%s type does not exist" % type
            raise Exception()
        
        self.vals['type_id'] = val[0]
        
        self.checkForAttackAlready()
        
    def addHit(self, vals):
        """  """
        hit = DBAddHit(self.connection, self.cursor)
        self.vals['hit_type'], self.vals['hit_id'] = hit.execute(vals)
        
    def addDamage(self, vals):
        """  """
        damage = DBAddDamage(self.connection, self.cursor)
        self.vals['damage_type'], self.vals['damage_id'] = damage.execute(vals)
        
    def addCrit(self, vals):
        """  """
        crit = DBAddCrit(self.connection, self.cursor)
        self.vals['crit_type'], self.vals['crit_id'] = crit.execute(vals)
        
    def addSpeed(self, vals):
        """  """
        speed = DBAddSpeed(self.connection, self.cursor)
        self.vals['speed_type'], self.vals['speed_id'] = speed.execute(vals)
        
    def addEffect(self, vals):
        """  """
        effect = DBAddEffect(self.connection, self.cursor)
        effect_type, effect_id = effect.execute(vals)
        self.vals['effects'].append((effect_type, effect_id,))
        
    def checkForAttackAlready(self):
        """  """
        self.cursor.execute("SELECT id from Attack where name = ?", (self.vals['name'],))
        t = self.cursor.fetchone()
        
        if not t is None:
            print "Attack %s already exists" % self.vals['name']
            raise Exception()