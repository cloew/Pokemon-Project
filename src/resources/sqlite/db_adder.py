import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID

class DBAdder:
    """  """
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
    
    def execute(self, params):
        """  """
        type = params[0]
        type_id = self.getTypeID(type)
        
        id = self.getIDForType[type](params[1:])
        
        return type_id, id
        
    def getTypeID(self, type):
        """ Checks the Type Exists before and returns its id """
        typeExists = CheckForType(self.cursor, type, self.variantTable)
        if typeExists is None:
            print "%s type %s does not exist." % (self.delegateType, type)
            exit(-2)
        
        return typeExists[0]
            
    def getID(self, table, where, params):
        """  """
        return GetID(self.cursor, table, where, params)
        
    def printBuilding(self, type, vals):
        """  """
        t = (type,  self.delegateType) + vals
        print "Building %s %s delegate with priority %s" %  t
        
    def buildDelegate(self, type, table, where, toAdd, params):
        """  """
        exists = self.getID(table, where, toAdd)
         
        if exists is None:
            self.printBuilding(type, toAdd)
            self.cursor.execute("INSERT INTO %s (%s) values(?)" % (table, params), toAdd )
            self.connection.commit()
            exists = self.getID(table, where, toAdd)
        else:
            print "%s Variant %s already exists! Using that!" % (self.delegateType, type)
        return exists[0]