import sqlite3
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect
from resources.sqlite.db_add_hit import DBAddHit

class DBAddAttack:
    """ Adds an attack to the Database """
    def __init__(self):
        """  """
        self.commands = {'p':self.addParameters, 'h':self.addHit,
                                   'd':self.addDamage, 'c':self.addCrit, 's':self.addSpeed}
        self.vals = {'name':None, 'type':None,
                          'hit_type':None, 'hit_id':None}
        
        
        self.connection = PkmnDBConnect()
        self.cursor = self.connection.cursor()
    
    def execute(self, params):
        """  """
        for param in params:
            cmd = param[0]
            cmdParams = param[2:].split(':')
            
            self.commands[cmd](cmdParams)
            
        self.connection.close()
            
    def addParameters(self, vals):
        """ Adds Attack specific parameters """
        self.vals['name'] = vals[0]
        self.vals['type'] = vals[1]
        
        self.checkForAttackAlready()
        
    def addHit(self, vals):
        """  """
        hit = DBAddHit(self.connection, self.cursor)
        self.vals['hit_type'], self.vals['hit_id'] = hit.execute(vals)
        
    def addDamage(self, vals):
        """  """
        print vals
        
    def addCrit(self, vals):
        """  """
        print vals
        
    def addSpeed(self, vals):
        """  """
        print vals
        
    def checkForAttackAlready(self):
        """  """
        self.cursor.execute("SELECT id from Attack where name = ?", (self.vals['name'],))
        t = self.cursor.fetchone()
        
        if not t is None:
            print "Attack %s already exists" % self.vals['name']
            exit(-2)