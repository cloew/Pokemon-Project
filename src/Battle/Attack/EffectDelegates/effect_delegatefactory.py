from applylock_delegate import ApplyLockDelegate
from charge_delegate import ChargeDelegate
from chance_delegate import ChanceDelegate
from applystatus_delegate import ApplyStatusDelegate
from confuse_delegate import ConfuseDelegate
from critmod_delegate import CritModDelegate
from curestatus_delegate import CureStatusDelegate
from dodge_delegate import DodgeDelegate
from flinch_delegate import FlinchDelegate
from heal_damageratio_delegate import HealByDamageRatioDelegate
from heal_hpratio_delegate import HealByHPRatioDelegate
from leech_delegate import LeechDelegate
from null_effect_delegate import NullEffectDelegate
from periodicheal_delegate import PeriodicHealDelegate
from randomstatmod_delegate import RandomStatModDelegate
from recoil_delegate import RecoilDelegate
from reset_statmods_delegate import ResetStatModsDelegate
from selfdestruct_delegate import SelfDestructDelegate
from statmod_delegate import StatModDelegate
from swapstatmods_delegate import SwapStatModsDelegate
from trap_delegate import TrapDelegate

from resources.tags import Tags
from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory


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
            delegate = ApplyLockDelegate(turns, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "CHANCE":
            chance = int(element.find(Tags.chanceTag).text)
            effects = []
            effectDelegates = element.find(Tags.effectDelegatesTag)
            for effectDelegate in effectDelegates.getchildren():
                effects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
            delegate = ChanceDelegate(chance, effects)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
        elif delegateType == "CHARGE":
            turns = int(element.find(Tags.turnsTag).text)
            hitOnTurn = int(element.find(Tags.hitOnTurnTag).text)
            message = element.find(Tags.messageTag).text
            delegate = ChargeDelegate(turns, hitOnTurn, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "CONFUSE":
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = ConfuseDelegate(affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
                
        elif delegateType == "CRIT MOD":
            stat = element.find(Tags.statTag).text
            degree = int(element.find(Tags.degreeTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = CritModDelegate(stat, degree, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "CURE STATUS":
            status = element.find(Tags.statusTag).text
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = CureStatusDelegate(status, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "DAMAGE IS EFFECT":
            parent.damageDelegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return parent.damageDelegate
            
        elif delegateType == "DODGE":
            dodgeType = element.find(Tags.dodgeTypeTag).text
            message = element.find(Tags.messageTag).text
            delegate = DodgeDelegate(dodgeType, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
            
        elif delegateType == "FLINCH":
            delegate = FlinchDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.TARGET)
            return delegate
            
        elif delegateType == "HEAL DAMAGE RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            delegate = HealByDamageRatioDelegate(healRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "HEAL HP RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            delegate = HealByHPRatioDelegate(healRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "LEECH":
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            delegate = LeechDelegate(startMessage, message, parent.type)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "RND STAT MOD":
            degree = int(element.find(Tags.degreeTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = RandomStatModDelegate(degree, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "RECOIL":
            recoilRatio = int(element.find(Tags.ratioTag).text)
            delegate = RecoilDelegate(recoilRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "RESET STAT MODS":
            delegate = ResetStatModsDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
        elif delegateType == "PERIODIC HEAL":
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            delegate = PeriodicHealDelegate(startMessage, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "SELFDESTRUCT":
            return SelfDestructDelegate()
            
        elif delegateType == "STAT MOD":
            stat = element.find(Tags.statTag).text
            degree = int(element.find(Tags.degreeTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = StatModDelegate(stat, degree, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "STATUS":
            status = element.find(Tags.statusTag).text
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = ApplyStatusDelegate(parent, status, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "SWAP STAT MODS":
            delegate = SwapStatModsDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.EITHER)
            return delegate
            
        elif delegateType == "TRAP":    
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            doneMessage = element.find(Tags.doneMessageTag).text
            delegate = TrapDelegate(startMessage, message, doneMessage)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.TARGET)
            return delegate