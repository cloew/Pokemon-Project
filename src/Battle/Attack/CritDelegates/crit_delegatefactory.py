import sqlite3

from Battle.Attack.CritDelegates.crit_delegate import CritDelegate

from resources.tags import Tags

class CritDelegateFactory:
    """ Builds Crit Delegates """
            
    @staticmethod
    def loadFromXML(element):
        """ Builds a critDelegate for the damageDelegate """
        delegate = element.find(Tags.damageDelegateTag)
        delegate = element.find(Tags.critDelegateTag)
        base = int(delegate.find(Tags.baseTag).text)
        return CritDelegate(base)
        
    @staticmethod
    def loadFromDB(cursor, parent):
        """ Loads an attack Crit Delegate from a Database """
        type, id = CritDelegateFactory.GetTypeAndID(cursor, parent.name)
        
        if type == "CORE":
            cursor.execute("SELECT base from CoreCritDelegate where id=?", (id,))
            base = cursor.fetchone()[0]
            return CritDelegate(base)
        
        cursor.close()
        
    @staticmethod
    def GetTypeAndID(cursor, name):
        """ Returns the type and id of the Crit Delegate for the attack """
        cursor.execute("SELECT CritDelegateVariants.type, Attack.crit_id from Attack, CritDelegateVariants where CritDelegateVariants.id = Attack.crit_type and name = ?", (name,))
        return cursor.fetchone()
            
    @staticmethod
    def buildNull():
        """ Returns a Null crit delegate """
        return CritDelegate(0)