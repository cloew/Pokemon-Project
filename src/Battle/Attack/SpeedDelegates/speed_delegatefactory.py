from Battle.Attack.SpeedDelegates.speed_delegate import SpeedDelegate
from resources.tags import Tags

class SpeedDelegateFactory:    
    
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a DamageDelegate from XML """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "CORE":
            priority = int(element.find(Tags.priorityTag).text)
            return SpeedDelegate(parent, priority)
            
    @staticmethod
    def loadFromDB(cursor, parent):
        """ Builds a SpeedDelegate from database"""
        type, id = SpeedDelegateFactory.GetTypeAndID(cursor, parent.name)
        
        if type == "CORE":
            cursor.execute("SELECT priority from CoreSpeedDelegate where id = ?", (id,))
            priority = cursor.fetchone()[0]
            return SpeedDelegate(parent, priority)
        
    @staticmethod
    def GetTypeAndID(cursor, name):
        """ Returns the type and id of the Damage Delegate for the attack """
        cursor.execute("SELECT SpeedDelegateVariants.type, Attack.speed_id from Attack, SpeedDelegateVariants where SpeedDelegateVariants.id = Attack.speed_type and name = ?", (name,))
        return cursor.fetchone()
            
    @staticmethod
    def buildNull():
        """ Builds a Null Speed Delegate """
        return SpeedDelegate(None, 0)