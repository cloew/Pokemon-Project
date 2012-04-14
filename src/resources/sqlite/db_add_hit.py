import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddHit(DBAdder):
    """  """
    delegateType = "Hit"
    variantTable = "HitDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'ALWAYS':self.buildAlways,
                                       'CORE':self.buildCore,
                                       'PIERCE DODGE':self.buildPierceDodge,
                                       'SELF':self.buildSelf,
                                       'STATUS ALWAYS':self.buildAlways,
                                       'STATUS CORE':self.buildCore}
        
    def buildAlways(self, params):
        """  """
        return None
        
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreHitDelegate"
        acc = int(params[0])
        where = "accuracy = ?"
        toAdd = (acc,)
        params = "accuracy"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildPierceDodge(self, params):
        """  """
        type = "PIERCE DODGE"
        table = "PierceDodgeHit"
        acc = int(params[0])
        pierce = params[1]
        where = "accuracy = ? and pierce = ?"
        toAdd = (acc, pierce,)
        params = "accuracy, pierce"
        
        return self.buildDelegate(type, table, where, toAdd, params)
        
    def buildSelf(self, params):
        """  """
        return None