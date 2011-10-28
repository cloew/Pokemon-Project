from Battle.Attack.EffectDelegates.applylock_delegate import ApplyLockDelegate
from Battle.Attack.EffectDelegates.charge_delegate import ChargeDelegate
from Battle.Attack.EffectDelegates.chance_delegate import ChanceDelegate
from Battle.Attack.EffectDelegates.applystatus_delegate import ApplyStatusDelegate
from Battle.Attack.EffectDelegates.critmod_delegate import CritModDelegate
from Battle.Attack.EffectDelegates.dodge_delegate import DodgeDelegate
from Battle.Attack.EffectDelegates.flinch_delegate import FlinchDelegate
from Battle.Attack.EffectDelegates.heal_damageratio_delegate import HealByDamageRatioDelegate
from Battle.Attack.EffectDelegates.heal_hpratio_delegate import HealByHPRatioDelegate
from Battle.Attack.EffectDelegates.null_effect_delegate import NullEffectDelegate
from Battle.Attack.EffectDelegates.recoil_delegate import RecoilDelegate
from Battle.Attack.EffectDelegates.reset_statmods_delegate import ResetStatmodsDelegate
from Battle.Attack.EffectDelegates.selfdestruct_delegate import SelfDestructDelegate
from Battle.Attack.EffectDelegates.statmod_delegate import StatModDelegate
from Battle.Attack.EffectDelegates.swapstatmods_delegate import SwapStatModsDelegate
from Battle.Attack.EffectDelegates.trap_delegate import TrapDelegate

from resources.tags import Tags


class EffectDelegateFactory:
    """ Builds EffectDelegates """
    
    @staticmethod
    def loadFromAttackDex(attackdex):
        """ Builds a HitDelegate from a file of the designated type """
        delegateType = attackdex.readline().strip()
        
        if delegateType == "STAT MOD":
            effects = attackdex.readline().strip().split(" ")
            return StatModDelegate(effects[0], int(effects[1]), int(effects[2]))
        if delegateType == "NULL":
            return NullEffectDelegate()
            
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a HitDelegate from a XML file """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "APPLY LOCK":
            turns = int(element.find(Tags.turnsTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            return ApplyLockDelegate(turns, affectUser)
            
        elif delegateType == "CHANCE":
            chance = int(element.find(Tags.chanceTag).text)
            effects = []
            effectDelegates = element.find(Tags.effectDelegatesTag)
            for effectDelegate in effectDelegates.getchildren():
                effects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
            
            return ChanceDelegate(chance, effects)
            
        elif delegateType == "CHARGE":
            turns = int(element.find(Tags.turnsTag).text)
            hitOnTurn = int(element.find(Tags.hitOnTurnTag).text)
            message = element.find(Tags.messageTag).text
            return ChargeDelegate(turns, hitOnTurn, message)
                
        elif delegateType == "CRIT MOD":
            stat = element.find(Tags.statTag).text
            degree = int(element.find(Tags.degreeTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            return CritModDelegate(stat, degree, affectUser)
            
        elif delegateType == "DAMAGE IS EFFECT":
            return parent.damageDelegate
            
        elif delegateType == "DODGE":
            dodgeType = element.find(Tags.dodgeTypeTag).text
            message = element.find(Tags.messageTag).text
            return DodgeDelegate(dodgeType, message)
            
        elif delegateType == "FLINCH":
            return FlinchDelegate()
            
        elif delegateType == "HEAL DAMAGE RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            return HealByDamageRatioDelegate(healRatio)
            
        elif delegateType == "HEAL HP RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            return HealByHPRatioDelegate(healRatio)
            
        elif delegateType == "RECOIL":
            recoilRatio = int(element.find(Tags.ratioTag).text)
            return RecoilDelegate(recoilRatio)
            
        elif delegateType == "RESET STAT MODS":
            return ResetStatmodsDelegate()
            
        elif delegateType == "SELFDESTRUCT":
            return SelfDestructDelegate()
            
        elif delegateType == "STAT MOD":
            stat = element.find(Tags.statTag).text
            degree = int(element.find(Tags.degreeTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            return StatModDelegate(stat, degree, affectUser)
            
        elif delegateType == "STATUS":
            status = element.find(Tags.statusTag).text
            affectUser = int(element.find(Tags.affectUserTag).text)
            return ApplyStatusDelegate(parent, status, affectUser)
            
        elif delegateType == "SWAP STAT MODS":
            return SwapStatModsDelegate()
            
        elif delegateType == "TRAP":    
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            return TrapDelegate(startMessage, message)