import xml.etree.ElementTree

from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory

from accmod_ability import AccModAbility
from booststab_ability import BoostStabAbility
from cantlowerstat_ability import CantLowerStatAbility
from effectafterturn_ability import EffectAfterTurnAbility
from effectoncrit_ability import EffectOnCritAbility
from nocrit_ability import NoCritAbility
from skip_turn_ability import SkipTurnAbility
from sniper_ability import SniperAbility
from statmodonstatus_ability import StatModOnStatusAbility

from resources.tags import Tags

class AbilityFactory:
    """ Builds Abilities """
    
    @staticmethod
    def loadFromPkmnXML(name):
        """ Load an ability with the given name from an XML file """
        # Get Ability XML
        tree = AbilityFactory.getAbilitydexTree()
        tree = AbilityFactory.getAbilityXML(tree, name)
        
        # Build the Ability
        ability = AbilityFactory.buildAbilityFromXML(tree)
        return ability
    
    @staticmethod
    def getAbilitydexTree():
        """ Opens the attackdex.xml file as an element tree """
        try:
            abilitydex = open("resources/abilitydex.xml", 'r')
        except IOError:
            print "Unable to open ABILITYDEX"
            exit(-2)
    
        tree = xml.etree.ElementTree.ElementTree(file=abilitydex)
        abilitydex.close()
        return tree
        
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
            
        elif abilityType == "EFFECT AFTER TURN":
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectAfterTurnAbility(name, effects)
            
        elif abilityType == "EFFECT ON CRIT":
            effectsTree = tree.find(Tags.effectDelegatesTag)
            effects = []
        
            for effectTree in effectsTree.getchildren():
                effect = EffectDelegateFactory.loadFromXML(effectTree, None)
                effects.append(effect)
                
            return EffectOnCritAbility(name, effects)
            
        elif abilityType == "NO CRIT":
            return NoCritAbility(name)
            
        elif abilityType == "SKIP TURN":
            return SkipTurnAbility()
            
        elif abilityType == "SNIPER":
            return SniperAbility(name)
        
        elif abilityType == "STAT MOD ON STATUS":
            status = tree.find(Tags.statusTag).text
            stat = tree.find(Tags.statTag).text
            mod = float(tree.find(Tags.degreeTag).text)
            return StatModOnStatusAbility(name, status, stat, mod)