import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID

class DBAddHit:
    """  """
    variantTable = "HitDelegateVariants"
    
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        
        self.getIDForType = {'CORE':self.buildCore}
    
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
            print "Hit type %s does not exist." % type
            exit(-2)
        
        return typeExists[0]
        
    def buildCore(self, params):
        """  """
        table = "CoreHitDelegate"
        acc = int(params[0])
        
        exists = GetID(self.cursor, table, "accuracy = ?", (acc,))
         
        if exists is None:
            print "Building CORE delegate with accuracy %s" % acc
            self.cursor.execute("INSERT INTO %s (accuracy) values(?)" % table, (acc,) )
            self.connection.commit()
            exists = GetID(self.cursor, table, "accuracy = ?", (acc,))
        else:
            print "Hit already exists! Using that!"
        return exists[0]
            
            
    def getID(self, table, where, params):
        """  """
        self.cursor.execute("SELECT id from %s where %s" % (table, where), params)
        return self.cursor.fetchone()