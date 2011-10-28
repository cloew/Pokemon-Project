from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.damagescale_delegate import DamageScaleDelegate
from Battle.Attack.DamageDelegates.effect_ondamage_delegate import EffectOnDamageDelegate
from Battle.Attack.DamageDelegates.fixed_delegate import FixedDelegate
from Battle.Attack.DamageDelegates.halfhealth_delegate import HalfHealthDelegate
from Battle.Attack.DamageDelegates.level_delegate import LevelDelegate
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate
from Battle.Attack.DamageDelegates.onehit_delegate import OneHitDelegate
from Battle.Attack.DamageDelegates.piercedodge_2Xdelegate import PierceDodge2XDelegate
from Battle.Attack.DamageDelegates.statratio_delegate import StatRatioDelegate


from Battle.Attack.CritDelegates.crit_delegate import CritDelegate

from resources.tags import Tags

class DamageDelegateFactory:
    """ Builds HitDelegates """
    
    @staticmethod
    def loadFromAttackDex(attackdex, parent):
        """ Builds a HitDelegate from a file of the designated type """
        delegateType = attackdex.readline().strip()
        
        if delegateType == "CORE":
            power = int(attackdex.readline().strip())
            parent.critDelegate = CritDelegate(int(attackdex.readline().strip()))
            return DamageDelegate(parent, power)
        if delegateType == "NULL":
            return NullDamageDelegate()
            
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a DamageDelegate from XML """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "CORE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return DamageDelegate(parent, power, isPhysical)
            
        elif delegateType == "EFFECT ON DAMAGE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return EffectOnDamageDelegate(parent, power, isPhysical)
        
        elif delegateType == "FIXED":
            isPhysical = int(element.find(Tags.physicalTag).text)
            damage = int(element.find(Tags.damageTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return FixedDelegate(parent, damage, isPhysical)
            
        elif delegateType == "HALF HEALTH":
            isPhysical = int(element.find(Tags.physicalTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return HalfHealthDelegate(parent, isPhysical)
        
        elif delegateType =="LEVEL":
            isPhysical = int(element.find(Tags.physicalTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return LevelDelegate(parent, isPhysical)
            
        elif delegateType == "ONE HIT KO":
            isPhysical = int(element.find(Tags.physicalTag).text)
            return OneHitDelegate(parent, isPhysical)
            
        elif delegateType == "PIERCE DODGE 2X":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            pierce = element.find(Tags.pierceTag).text
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return PierceDodge2XDelegate(parent, power, isPhysical, pierce)
            
        elif delegateType == "SCALE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            factor = int(element.find(Tags.factorTag).text)
            turns = int(element.find(Tags.turnsTag).text)
            return DamageScaleDelegate(parent, power, isPhysical, factor, turns)
            
        elif delegateType == "STAT RATIO":
            isPhysical = int(element.find(Tags.physicalTag).text)
            stat = element.find(Tags.statTag).text
            parent.critDelegate = DamageDelegateFactory.buildCritDelegate(element)
            return StatRatioDelegate(parent, isPhysical, stat)
            
        
            
        
            
    @staticmethod
    def buildNull():
        """ Returns a Null damage delegate """
        return NullDamageDelegate()
            
    @staticmethod
    def buildCritDelegate(element):
        """ Builds a critDelegate for the damageDelegate """
        delegate = element.find(Tags.critDelegateTag)
        base = int(delegate.find(Tags.baseTag).text)
        return CritDelegate(base)