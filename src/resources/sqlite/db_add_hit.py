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
        toAdd = (acc,)
        params = "accuracy"
        
        return self.buildDelegate(type, table, where, toAdd, params)