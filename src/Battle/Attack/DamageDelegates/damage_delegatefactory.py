import sqlite3

from Battle.Attack.attack import Attack

from Battle.Attack.DamageDelegates.boost_on_status_delegate import BoostDamageOnStatusDelegate
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.damagescale_delegate import DamageScaleDelegate
from Battle.Attack.DamageDelegates.effect_ondamage_delegate import EffectOnDamageDelegate
from Battle.Attack.DamageDelegates.fixed_delegate import FixedDelegate
from Battle.Attack.DamageDelegates.halfhealth_delegate import HalfHealthDelegate
from Battle.Attack.DamageDelegates.level_delegate import LevelDelegate
from Battle.Attack.DamageDelegates.no_faint_delegate import NoFaintDelegate
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate
from Battle.Attack.DamageDelegates.onehit_delegate import OneHitDelegate
from Battle.Attack.DamageDelegates.piercedodge_2Xdelegate import PierceDodge2XDelegate
from Battle.Attack.DamageDelegates.statratio_fixed_delegate import StatRatioFixedDelegate
from Battle.Attack.DamageDelegates.statratio_range_delegate import StatRatioRangeDelegate


from Battle.Attack.CritDelegates.crit_delegate import CritDelegate

from resources.tags import Tags

class DamageDelegateFactory:
    """ Builds DamageDelegates """
            
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a DamageDelegate from XML """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "BOOST ON STATUS":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            return BoostDamageOnStatusDelegate(parent, power, isPhysical)
        
        elif delegateType == "CORE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            return DamageDelegate(parent, power, isPhysical)
            
        elif delegateType == "EFFECT ON DAMAGE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            return EffectOnDamageDelegate(parent, power, isPhysical)
        
        elif delegateType == "FIXED":
            isPhysical = int(element.find(Tags.physicalTag).text)
            damage = int(element.find(Tags.damageTag).text)
            return FixedDelegate(parent, damage, isPhysical)
            
        elif delegateType == "HALF HEALTH":
            isPhysical = int(element.find(Tags.physicalTag).text)
            return HalfHealthDelegate(parent, isPhysical)
        
        elif delegateType =="LEVEL":
            isPhysical = int(element.find(Tags.physicalTag).text)
            return LevelDelegate(parent, isPhysical)
            
        elif delegateType == "NO FAINT":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            return NoFaintDelegate(parent, power, isPhysical)
            
        elif delegateType == "ONE HIT KO":
            isPhysical = int(element.find(Tags.physicalTag).text)
            return OneHitDelegate(parent, isPhysical)
            
        elif delegateType == "PIERCE DODGE 2X":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            pierce = element.find(Tags.pierceTag).text
            return PierceDodge2XDelegate(parent, power, isPhysical, pierce)
            
        elif delegateType == "SCALE":
            power = int(element.find(Tags.powerTag).text)
            isPhysical = int(element.find(Tags.physicalTag).text)
            factor = int(element.find(Tags.factorTag).text)
            turns = int(element.find(Tags.turnsTag).text)
            return DamageScaleDelegate(parent, power, isPhysical, factor, turns)
            
        elif delegateType == "STAT RATIO FIXED":
            isPhysical = int(element.find(Tags.physicalTag).text)
            stat = element.find(Tags.statTag).text
            return StatRatioFixedDelegate(parent, isPhysical, stat)
            
        elif delegateType == "STAT RATIO RANGE":
            isPhysical = int(element.find(Tags.physicalTag).text)
            stat = element.find(Tags.statTag).text
            return StatRatioRangeDelegate(parent, isPhysical, stat)
            
        
    @staticmethod
    def loadFromDB(cursor, parent):
        """ Loads an attack Damage Delegate from a Database """
        type, id = DamageDelegateFactory.GetTypeAndID(cursor, parent.name)
        
        if type == "CORE":
            cursor.execute("SELECT power, physical from CoreDamageDelegate where id=?", (id,))
            power, physical = cursor.fetchone()
            return DamageDelegate(None, power, physical)
        
        cursor.close()
        
    @staticmethod
    def GetTypeAndID(cursor, name):
        """ Returns the type and id of the Damage Delegate for the attack """
        cursor.execute("SELECT DamageDelegateVariants.type, Attack.damage_id from Attack, DamageDelegateVariants where DamageDelegateVariants.id = Attack.damage_type and name = ?", (name,))
        return cursor.fetchone()
            
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
        
    @staticmethod
    def getConfusionAttack():
        """  Builds and returns the DamageDelegate used for Confusion """
        attack = Attack()
        attack.type = ""
        return DamageDelegate(attack, 40, 1)