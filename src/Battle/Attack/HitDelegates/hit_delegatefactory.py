from Battle.Attack.HitDelegates.alwayshit_delegate import AlwaysHitDelegate
from Battle.Attack.HitDelegates.crash_delegate import CrashDelegate
from Battle.Attack.HitDelegates.hit_delegate import HitDelegate
from Battle.Attack.HitDelegates.hitself_delegate import HitSelfDelegate
from Battle.Attack.HitDelegates.piercedodge_delegate import PierceDodgeDelegate


from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory

from resources.tags import Tags

class HitDelegateFactory:
    """ Builds HitDelegates """
    
    MISS = "Attack missed."
    STATUSMISS = "But it failed."
    
    @staticmethod
    def loadFromAttackDex(attackdex, parent):
        """ Builds a HitDelegate from a file of the designated type """
        delegateType = attackdex.readline().strip()
        
        if delegateType == "CORE":
            accuracy = int(attackdex.readline().strip())
            return HitDelegate(parent, accuracy, "Attack missed.")
            
        elif delegateType == "STATUS CORE":
            accuracy = int(attackdex.readline().strip())
            return HitDelegate(parent, accuracy, "But it failed.")
            
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a HitDelegate from XML """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.MISS)
        
        elif delegateType == "CORE":
            accuracy = int(element.find(Tags.hitTag).text)
            return HitDelegate(parent, accuracy, HitDelegateFactory.MISS)
            
        elif delegateType == "CRASH":
            accuracy = int(element.find(Tags.hitTag).text)
            element = element.find(Tags.effectDelegateTag)
            delegate = EffectDelegateFactory.loadFromXML(element, parent)
            return CrashDelegate(parent, accuracy, HitDelegateFactory.MISS, delegate)
            
        elif delegateType == "PIERCE DODGE":
            accuracy = int(element.find(Tags.hitTag).text)
            pierce = element.find(Tags.pierceTag).text
            return PierceDodgeDelegate(parent, accuracy, HitDelegateFactory.MISS, pierce)
            
        elif delegateType == "SELF":
            return HitSelfDelegate()
            
        elif delegateType == "STATUS ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.STATUSMISS)
            
        elif delegateType == "STATUS CORE":
            accuracy = int(element.find(Tags.hitTag).text)
            return HitDelegate(parent, accuracy, HitDelegateFactory.STATUSMISS)
            
    @staticmethod
    def buildNull():
        """ Returns a Null hit delegate """
        """ May not need """
        return None