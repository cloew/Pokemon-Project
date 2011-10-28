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