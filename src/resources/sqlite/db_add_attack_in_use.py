import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

from resources.sqlite.db_adder import DBAdder

class DBAddAttackInUse(DBAdder):
    """ Adds an Attack In Use to the Database """
    def __init__(self, id, connection = None, cursor = None):
        """  """
        self.delegateType = "Attack in Use"
        self.commands = {'p':self.addParameters}
        self.vals = {'pkmn_id':id, 
                          'attack_id':None}
        
        #self.pkmn_id = id
        if connection is None:
            self.connection = PkmnDBConnect()
            self.cursor = self.connection.cursor()
        else:
            self.connection = connection
            self.cursor = cursor
    
    def execute(self, params, close = True):
        """  """
        self.attack = params[0]
        self.cursor.execute("SELECT id from Attack where name = ?", (self.attack,))
        self.vals['attack_id'] = self.cursor.fetchone()[0]
            
        self.addAttackInUse()
            
        self.connection.commit()
        
        if (close):
            self.connection.close()
        
    def addAttackInUse(self):
        """ Adds the attack to the database """
        params = []
        toAdd = []
        
        for key in self.vals.keys():
            if self.vals[key] is None:
                continue 
                
            params += [key]
            toAdd += [self.vals[key]]
            
        paramStr = self.GetStrFromList(params)
        
        print "Adding Attack In Use:", self.attack
        self.insertIntoDB("AttackInUse", paramStr, toAdd)