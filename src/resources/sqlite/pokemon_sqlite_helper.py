import sqlite3

""" Helper methods to manage connection to the Pokemon Database """
    
def PkmnDBConnect():
    """ Connects to the Pokemon Database """
    connection = sqlite3.connect('resources/sqlite/pokemon.sqlite')
    connection.text_factory = str
    
    return connection
        
def GetParameters(cursor, parameters, table, id):
    """ Returns the parameters from the table row with the id """
    if type(parameters) is list:
        ret = GetParametersFromList(cursor, parameters, table, id)
    else:
        ret = GetParametersFromStr(cursor, parameters, table, id)
        
    return ret
    
def GetParametersFromList(cursor, parameters, table, id):
    """ Gets parameters from a tuple """
    message = ""
    
    for param in parameters:
        if not message == "":
            message += ", "
        message += param
        
    return Execute(cursor, message, table, id)
    
def GetParametersFromStr(cursor, param, table, id):
    """ Gets parameters from a single String """
    return Execute(cursor, param, table, id)[0]
    
def Execute(cursor, param, table, id):
    """ Executes a DB Query """
    cursor.execute("SELECT %s from %s where id = ?" % (param, table), (id,))
    return cursor.fetchone()
    
def CheckForType(cursor, type, variantTable):
    """ Returns if the type exists in the Variant Table """
    cursor.execute("SELECT id from %s where type = ?" % variantTable, (type,))
    return cursor.fetchone()

def GetID(cursor, table, where, params):
        """  """
        cursor.execute("SELECT id from %s where %s" % (table, where), params)
        return cursor.fetchone()