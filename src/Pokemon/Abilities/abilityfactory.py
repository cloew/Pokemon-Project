import xml.etree.ElementTree

from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory

from ability import Ability
from accmod_ability import AccModAbility
from booststab_ability import BoostStabAbility
from cantlowerstat_ability import CantLowerStatAbility
from confusion_immunity_ability import ConfusionImmunityAbility
from effectafterturn_ability import EffectAfterTurnAbility
from effecton_contact_ability import EffectOnContactAbility
from effectoncrit_ability import EffectOnCritAbility
from effecton_statmod_ability import EffectOnStatModAbility
from nocrit_ability import NoCritAbility
from resist_type_ability import ResistTypeAbility
from skip_turn_ability import SkipTurnAbility
from sniper_ability import SniperAbility
from statmodonstatus_ability import StatModOnStatusAbility

from resources.resource_manager import GetResourcePath
from resources.tags import Tags

class AbilityFactory:
    """ Builds Abilities """
    tree = None
    
    @staticmethod
    def loadFromPkmnXML(name):
        """ Load an ability with the given name from an XML file """
        # Get Ability XML
        tree = AbilityFactory.getAbilitydexTree()
        tree = AbilityFactory.getAbilityXML(tree, name)
        
        # Build the Ability
        if tree == None:
            print "Could not find ability:", name
            ability = Ability()
        else:
            ability = AbilityFactory.buildAbilityFromXML(tree)
        return ability
    
    @staticmethod
    def getAbilitydexTree():
        """ Opens the attackdex.xml file as an element tree """
        if AbilityFactory.tree is not None:
            return AbilityFactory.tree
        
        try:
            abilitydex = open(GetResourcePath("abilitydex.xml"), 'r')
        except IOError:
            print "Unable to open ABILITYDEX"
            exit(-2)
    
        AbilityFactory.tree = xml.etree.ElementTree.ElementTree(file=abilitydex)
        abilitydex.close()
        return AbilityFactory.tree
        
    @staticmethod
    def getAbilityXML(tree, name):
        """ Returns the XML tree for the attack with the name given """
        for ability in tree.getiterator(Tags.abilityTag):
            if ability.find(Tags.nameTag).text == name:
                return ability
            
    @staticmethod
    def buildAbilityFromXML(tree):
        """ Builds a DamageDelegate from XML """
        name = tree.find(Tags.nameTag).text
        abilityType = tree.find(Tags.typeTag).text
        
        if abilityType == "ACC MOD":
            mod = float(tree.find(Tags.degreeTag).text)
            return AccModAbility(name, mod)
        
        elif abilityType == "BOOST STAB":
            return BoostStabAbility(name)
        
        elif abilityType == "CANT LOWER STAT":
            stat = tree.find(Tags.statTag).text
            return CantLowerStatAbility(name, stat)
            
        elif abilityType == "CONFUSION IMMUNITY":
            return ConfusionImmunityAbility(name)
          
        elif abilityType == "DEFENSE EFFECTIVENESS":
            entries = {}
            effectivenessTree = tree.find(Tags.effectivenessesTag)
            for entry in effectivenessTree.getchildren():
                type = entry.find(Tags.typeTag).text
                effectiveness = float(entry.find(Tags.effectivenessTag).text)
                message = entry.find(Tags.messageTag).text
                entries[type] = {}
                entries[type]['effectiveness'] = effectiveness
                entries[type]['message'] = message
            return ResistTypeAbility(name, entries)
          
        elif abilityType == "EFFECT AFTER TURN":
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectAfterTurnAbility(name, effects)
        
        elif abilityType == "EFFECT ON CONTACT":
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectOnContactAbility(name, effects)
        
        elif abilityType == "EFFECT ON CRIT":
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectOnCritAbility(name, effects)
            
        elif abilityType == "EFFECT ON STAT MOD":
            message  =  tree.find(Tags.messageTag).text
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectOnStatModAbility(name, effects, message)
            
        elif abilityType == "NO CRIT":
            return NoCritAbility(name)
            
        elif abilityType == "SKIP TURN":
            return SkipTurnAbility(name)
            
        elif abilityType == "SNIPER":
            return SniperAbility(name)
        
        elif abilityType == "STAT MOD ON STATUS":
            stat = tree.find(Tags.statTag).text
            mod = float(tree.find(Tags.degreeTag).text)
            return StatModOnStatusAbility(name, stat, mod)