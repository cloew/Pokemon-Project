import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddSpeed(DBAdder):
    """  """
    delegateType = "Speed"
    variantTable = "SpeedDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'CORE':self.buildCore}
        
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreSpeedDelegate"
        priority = int(params[0])
        where = "priority = ?"
        toAdd = (priority,)
        params = "priority"
        
        return self.buildDelegate(type, table, where, toAdd, params)