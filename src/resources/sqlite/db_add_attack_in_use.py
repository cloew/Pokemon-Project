import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder

class DBAddAttackInUse(DBAdder):
    """ Adds an Attack In Use to the Database """
    def __init__(self):
        """  """
        self.delegateType = "Attack in Use"
        self.commands = {'p':self.addParameters}
        self.vals = {'pkmn_id':None, 
                          'attack_id':None}
        
        
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
                
            params += [key]
            toAdd += [self.vals[key]]
            
        paramStr = self.GetStrFromList(params)
        
        print "Adding Attack In Use:", self.vals['']
        self.insertIntoDB("AttackInUse", paramStr, toAdd)
            
    def addParameters(self, vals):
        """ Adds Attack specific parameters """
        self.vals['pkmn_id'] = vals[0]
        self.name = vals[1]
        
        self.cursor.execute("SELECT id from Attack where name = ?", (self.name,))
        id = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT name from Pokemon where id = ?", (self.vals['pkmn_id'],)
        pkmn = self.cursor.fetchone()[0]
        
        print "Building Attack in Use %s for pkmn:" % self.name, pkmn
        
    def checkForAbilityAlready(self):
        """  """
        self.cursor.execute("SELECT id from Ability where name = ?", (self.vals['name'],))
        t = self.cursor.fetchone()
        
        if not t is None:
            print "Ability %s already exists" % self.vals['name']
            raise Exception()