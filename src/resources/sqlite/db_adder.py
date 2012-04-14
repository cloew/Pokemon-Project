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
        
    def printBuilding(self, type, params, toAdd):
        """  """
        t = (type,  self.delegateType, params, self.GetStrFromList(toAdd))
        print "Building %s %s delegate with %s: %s" %  t
        
    def buildDelegate(self, type, table, where, toAdd, params):
        """  """
        exists = self.getID(table, where, toAdd)
         
        if exists is None:
            self.printBuilding(type, params, toAdd)
            self.insertIntoDB(table, params, toAdd)
            exists = self.getID(table, where, toAdd)
        else:
            print "%s %s Delegate already exists! Using that!" % (type, self.delegateType)
        return exists[0]
        
    def insertIntoDB(self, table, params, toAdd):
        """  """
        qMarks = self.getQuestionMarks(len(toAdd))
            
        self.cursor.execute("INSERT INTO %s (%s) values(%s)" % (table, params, qMarks), toAdd )
        
    def getQuestionMarks(self, val):
        """  """
        qMarks = ""
        for i in range(val):
            if not qMarks == "":
                qMarks += ", "
            qMarks += "?"
        return qMarks
    
    def GetStrFromList(self, args):
        """ Combines the cmd list into a single string """
        cmdStr = ""
        for message in args:
            if not cmdStr == "":
                cmdStr += ", "
            cmdStr += str(message)
            
        return cmdStr