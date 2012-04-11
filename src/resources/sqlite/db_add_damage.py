import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddDamage(DBAdder):
    """  """
    delegateType = "Damage"
    variantTable = "DamageDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'CORE':self.buildCore}
        
    def buildCore(self, params):
        """  """
        table = "CoreDamageDelegate"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        
        exists = GetID(self.cursor, table, where, toAdd)
         
        if exists is None:
            print "Building CORE delegate with power %s and physical %s" % toAdd
            self.cursor.execute("INSERT INTO %s (power, physical) values(?, ?)" % table, toAdd)
            self.connection.commit()
            exists = GetID(self.cursor, table, where, toAdd)
        else:
            print "%s already exists! Using that!" % self.delegateType
        return exists[0]