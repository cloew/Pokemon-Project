from applylock_delegate import ApplyLockDelegate
from charge_delegate import ChargeDelegate
from chance_delegate import ChanceDelegate
from applystatus_delegate import ApplyStatusDelegate
from confuse_delegate import ConfuseDelegate
from critmod_delegate import CritModDelegate
from curestatus_delegate import CureStatusDelegate
from diverge_on_faint_delegate import DivergeOnFaintDelegate
from dodge_delegate import DodgeDelegate
from flinch_delegate import FlinchDelegate
from heal_damageratio_delegate import HealByDamageRatioDelegate
from heal_hpratio_delegate import HealByHPRatioDelegate
from leech_delegate import LeechDelegate
from multi_turn_fixed_delegate import FixedMultiTurnDelegate
from multi_turn_range_delegate import MultiTurnRangeDelegate
from null_effect_delegate import NullEffectDelegate
from periodicheal_delegate import PeriodicHealDelegate
from randomstatmod_delegate import RandomStatModDelegate
from random_switch_delegate import RandomSwitchDelegate
from recoil_delegate import RecoilDelegate
from reset_statmods_delegate import ResetStatModsDelegate
from selfdestruct_delegate import SelfDestructDelegate
from statmod_delegate import StatModDelegate
from swap_ability_delegate import SwapAbilityDelegate
from swap_stat_delegate import SwapStatDelegate
from swapstatmods_delegate import SwapStatModsDelegate
from switch_delegate import SwitchDelegate
from trap_delegate import TrapDelegate
from useless_delegate import UselessDelegate

from resources.tags import Tags
from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory


class EffectDelegateFactory:
    """ Builds EffectDelegates """
            
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
            effects = EffectDelegateFactory.getEffects(element, Tags.effectDelegatesTag, parent)
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
            degree = int(element.find(Tags.degreeTag).text)
            delegate = CritModDelegate(degree)
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
            
        elif delegateType == "DIVERGE ON FAINT":
            divergeEffectsXML = element.find(Tags.divergeEffectsTag)
            divergeEffects = []
            for effectDelegate in divergeEffectsXML.getchildren():
                divergeEffects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
                
            normalEffectsXML = element.find(Tags.normalEffectsTag)
            normalEffects = []
            for effectDelegate in normalEffectsXML.getchildren():
                normalEffects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
                
            delegate = DivergeOnFaintDelegate(divergeEffects, normalEffects)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
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
            
        elif delegateType == "MULTI TURN RANGE":
            min = int(element.find(Tags.minTag).text)
            max = int(element.find(Tags.maxTag).text)
            effects = EffectDelegateFactory.getEffects(element, Tags.effectDelegatesTag, parent)
            delegate = MultiTurnRangeDelegate(min, max, effects)
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
            
        elif delegateType == "RANDOM SWITCH":
            affectUser = int(element.find(Tags.affectUserTag).text)
            reset = int(element.find(Tags.resetTag).text)
            delegate = RandomSwitchDelegate(affectUser, reset)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "PERIODIC HEAL":
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            delegate = PeriodicHealDelegate(startMessage, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "SELFDESTRUCT":
            delegate = SelfDestructDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
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
            
        elif delegateType == "SWAP ABILITY":
            delegate = SwapAbilityDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.EITHER)
            return delegate
            
        elif delegateType == "SWAP STATS":
            stat1 = element.find(Tags.stat1Tag).text
            stat2 = element.find(Tags.stat2Tag).text
            delegate = SwapStatDelegate(stat1, stat2)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif delegateType == "SWAP STAT MODS":
            delegate = SwapStatModsDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.EITHER)
            return delegate
            
        elif delegateType == "SWITCH":
            affectUser = int(element.find(Tags.affectUserTag).text)
            reset = int(element.find(Tags.resetTag).text)
            delegate = SwitchDelegate(affectUser, reset)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif delegateType == "TRAP":    
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            doneMessage = element.find(Tags.doneMessageTag).text
            delegate = TrapDelegate(startMessage, message, doneMessage)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.TARGET)
            return delegate
            
        elif delegateType == "USELESS":
            delegate = UselessDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
    @staticmethod
    def loadAllEffectsFromDB(cursor, parent):
        """ Loads all Effects from a DB """
        effects = []
        for effectInfo in EffectDelegateFactory.GetTypeAndID(cursor, parent.name):
            effect = EffectDelegateFactory.loadFromDB(cursor, parent, effectInfo[0], effectInfo[1])
            effects.append(effect)
            
        return effects
            
    @staticmethod
    def loadFromDB(cursor, parent, type, id):
        """ Loads an Effect Delegate from a database """
        if type == "APPLY LOCK":
            turns = int(element.find(Tags.turnsTag).text)
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = ApplyLockDelegate(turns, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "CHANCE":
            chance = int(element.find(Tags.chanceTag).text)
            effects = EffectDelegateFactory.getEffects(element, Tags.effectDelegatesTag, parent)
            delegate = ChanceDelegate(chance, effects)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
        elif type == "CHARGE":
            turns = int(element.find(Tags.turnsTag).text)
            hitOnTurn = int(element.find(Tags.hitOnTurnTag).text)
            message = element.find(Tags.messageTag).text
            delegate = ChargeDelegate(turns, hitOnTurn, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "CONFUSE":
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = ConfuseDelegate(affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
                
        elif type == "CRIT MOD":
            cursor.execute("SELECT degree from CritModEffect where id = ?", (id,))
            degree = cursor.fetchone()[0]
            delegate = CritModDelegate(degree)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "CURE STATUS":
            status = element.find(Tags.statusTag).text
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = CureStatusDelegate(status, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "DAMAGE IS EFFECT":
            parent.damageDelegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return parent.damageDelegate
            
        elif type == "DIVERGE ON FAINT":
            divergeEffectsXML = element.find(Tags.divergeEffectsTag)
            divergeEffects = []
            for effectDelegate in divergeEffectsXML.getchildren():
                divergeEffects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
                
            normalEffectsXML = element.find(Tags.normalEffectsTag)
            normalEffects = []
            for effectDelegate in normalEffectsXML.getchildren():
                normalEffects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
                
            delegate = DivergeOnFaintDelegate(divergeEffects, normalEffects)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
        elif type == "DODGE":
            dodgeType = element.find(Tags.dodgeTypeTag).text
            message = element.find(Tags.messageTag).text
            delegate = DodgeDelegate(dodgeType, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "FLINCH":
            delegate = FlinchDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.TARGET)
            return delegate
            
        elif type == "HEAL DAMAGE RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            delegate = HealByDamageRatioDelegate(healRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "HEAL HP RATIO":
            healRatio = int(element.find(Tags.ratioTag).text)
            delegate = HealByHPRatioDelegate(healRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "LEECH":
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            delegate = LeechDelegate(startMessage, message, parent.type)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "MULTI TURN RANGE":
            min = int(element.find(Tags.minTag).text)
            max = int(element.find(Tags.maxTag).text)
            effects = EffectDelegateFactory.getEffects(element, Tags.effectDelegatesTag, parent)
            delegate = MultiTurnRangeDelegate(min, max, effects)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "RND STAT MOD":
            cursor.execute("SELECT degree, affectUser from RandomStatModEffect where id = ?", (id,))
            degree, affectUser = cursor.fetchone()
            delegate = RandomStatModDelegate(degree, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "RECOIL":
            recoilRatio = int(element.find(Tags.ratioTag).text)
            delegate = RecoilDelegate(recoilRatio)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "RESET STAT MODS":
            delegate = ResetStatModsDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.REGULAR)
            return delegate
            
        elif type == "RANDOM SWITCH":
            affectUser = int(element.find(Tags.affectUserTag).text)
            reset = int(element.find(Tags.resetTag).text)
            delegate = RandomSwitchDelegate(affectUser, reset)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "PERIODIC HEAL":
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            delegate = PeriodicHealDelegate(startMessage, message)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "SELFDESTRUCT":
            delegate = SelfDestructDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "STAT MOD":
            cursor.execute("SELECT stat, degree, affectUser from StatModEffect where id = ?", (id,))
            stat, degree, affectUser = cursor.fetchone()
            delegate = StatModDelegate(stat, degree, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "STATUS":
            status = element.find(Tags.statusTag).text
            affectUser = int(element.find(Tags.affectUserTag).text)
            delegate = ApplyStatusDelegate(parent, status, affectUser)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
        
        elif type == "SWAP ABILITY":
            delegate = SwapAbilityDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.EITHER)
            return delegate
            
        elif type == "SWAP STATS":
            stat1 = element.find(Tags.stat1Tag).text
            stat2 = element.find(Tags.stat2Tag).text
            delegate = SwapStatDelegate(stat1, stat2)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
        elif type == "SWAP STAT MODS":
            delegate = SwapStatModsDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.EITHER)
            return delegate
            
        elif type == "SWITCH":
            cursor.execute("SELECT reset, affectUser from SwitchEffect where id = ?", (id,))
            reset, affectUser = cursor.fetchone()
            delegate = SwitchDelegate(affectUser, reset)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.AFFECT_USER)
            return delegate
            
        elif type == "TRAP":    
            startMessage = element.find(Tags.startMessageTag).text
            message = element.find(Tags.messageTag).text
            doneMessage = element.find(Tags.doneMessageTag).text
            delegate = TrapDelegate(startMessage, message, doneMessage)
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.TARGET)
            return delegate
            
        elif type == "USELESS":
            delegate = UselessDelegate()
            delegate.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
            return delegate
            
    @staticmethod
    def GetTypeAndID(cursor, name):
        """ Returns the type and id of the Effect Delegates for the attack """
        return cursor.execute("SELECT EffectDelegateVariants.type, AttackEffectsJoin.effect_id from Attack, EffectDelegateVariants, AttackEffectsJoin where EffectDelegateVariants.id = AttackEffectsJoin.effect_type and Attack.id = AttackEffectsJoin.attack_id and name = ?", (name,))
           
    @staticmethod
    def getEffects(element, tag, parent):
        effects = []
        effectDelegates = element.find(tag)
        for effectDelegate in effectDelegates.getchildren():
            effects.append(EffectDelegateFactory.loadFromXML(effectDelegate, parent))
        return effects