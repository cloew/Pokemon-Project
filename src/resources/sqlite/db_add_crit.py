import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddCrit(DBAdder):
    """  """
    delegateType = "Crit"
    variantTable = "CritDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'CORE':self.buildCore}
        
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreCritDelegate"
        base = int(params[0])
        where = "base = ?"
        toAdd = (base,)
        params = "base"
        
        return self.buildDelegate(type, table, where, toAdd, params)