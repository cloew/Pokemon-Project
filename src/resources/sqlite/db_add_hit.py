import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddHit(DBAdder):
    """  """
    delegateType = "Hit"
    variantTable = "HitDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'CORE':self.buildCore}
        
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreHitDelegate"
        acc = int(params[0])
        where = "accuracy = ?"
        
        exists = self.getID(table, where, (acc,))
         
        if exists is None:
            print "Building %s delegate with accuracy %s" % (type, acc)
            self.cursor.execute("INSERT INTO %s (accuracy) values(?)" % table, (acc,) )
            self.connection.commit()
            exists = self.getID(table, where, (acc,))
        else:
            print "%s already exists! Using that!" % self.delegateType
        return exists[0]