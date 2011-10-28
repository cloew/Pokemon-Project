import xml.etree.ElementTree

from Battle.Attack.attack import Attack

from Battle.Attack.DamageDelegates.damage_delegatefactory import DamageDelegateFactory
from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory
from Battle.Attack.HitDelegates.hit_delegatefactory import HitDelegateFactory
from Battle.Attack.SpeedDelegates.speed_delegatefactory import SpeedDelegateFactory

from resources.tags import Tags

class AttackFactory:
    """ Builds an Attack, includng Delegates """
    factories = {Tags.hitDelegateTag:HitDelegateFactory,
                      Tags.damageDelegateTag:DamageDelegateFactory,
                      Tags.speedDelegateTag:SpeedDelegateFactory}
    
    @staticmethod
    def loadFromPokemonFile(file):
        """ Load an attack as saved within a Pokemon instance in a file """
        attack = Attack()
        try:
            attackdex = open("resources/ATTACKDEX.txt", 'r')
        except IOError:
            print "Unable to open ATTACKDEX"
            exit(-2)
      
        attack.name = file.readline().strip()
    
        temp = ""
        while (temp.find(attack.name) == -1):
            """ Read the file until you find the species we need """
            temp = attackdex.readline().strip()
    
        attack.type = attackdex.readline().strip()
        
        #Load delegates
        attack.hitDelegate = HitDelegateFactory.loadFromAttackDex(attackdex, attack)
        attack.damageDelegate = DamageDelegateFactory.loadFromAttackDex(attackdex, attack)
            
        attack.effectDelegate = EffectDelegateFactory.loadFromAttackDex(attackdex)
    
        # Get currPP and PP from file
        values = file.readline().strip().split(" ")
        attack.powerPoints = int(values[0])
        attack.currPowerPoints = int(values[1])    
                
        attackdex.close()
    
        return attack
        
    @staticmethod
    def loadFromPkmnXML(file):
        """ Load an attack as saved within a Pokemon instance in an XML file """
        # Get Attack XML
        name = file.readline().strip()
        tree = AttackFactory.getAttackdexTree()
        tree = AttackFactory.getAttackXML(tree, name)
        
        # Build the Attack
        attack = AttackFactory.buildAttackFromXML(tree)
    
        # Get currPP and PP from file
        values = file.readline().strip().split(" ")
        attack.powerPoints = int(values[0])
        attack.currPowerPoints = int(values[1])
    
        return attack
        
    @staticmethod
    def getAttackAsNew(name):
        """ Build an attack entirely from attackdex """
        # Get Attack XML
        tree = AttackFactory.getAttackdexTree()
        tree = AttackFactory.getAttackXML(tree, name)
        
        # Build the Attack
        attack = AttackFactory.buildAttackFromXML(tree)
    
        # Get currPP and PP from attackdex
        attack.powerPoints = int(tree.find(Tags.ppTag).text)
        attack.currPowerPoints = attack.powerPoints
    
        return attack
        
    @staticmethod
    def getAttackdexTree():
        """ Opens the attackdex.xml file as an element tree """
        try:
            attackdex = open("resources/attackdex.xml", 'r')
        except IOError:
            print "Unable to open ATTACKDEX"
            exit(-2)
    
        tree = xml.etree.ElementTree.ElementTree(file=attackdex)
        attackdex.close()
        return tree
        
    @staticmethod
    def getAttackXML(tree, name):
        """ Returns the XML tree for the attack with the name given """
        for attack in tree.getiterator(Tags.attackTag):
            if attack.find(Tags.nameTag).text == name:
                return attack
        
    @staticmethod
    def buildAttackFromXML(tree):
        """ Build an Attack from XML tree """
        attack = Attack()
        
        attack.name = tree.find(Tags.nameTag).text
        attack.type = tree.find(Tags.typeTag).text
        
        # Delegates
        for delegateCategory in AttackFactory.factories.keys():
            delegate = AttackFactory.getDelegate(tree, delegateCategory, attack)
            attack.addDelegate(delegateCategory, delegate)
            
        effects = tree.find(Tags.effectDelegatesTag)
        
        if effects:
            for effect in effects.getchildren():
                delegate = EffectDelegateFactory.loadFromXML(effect, attack)
                attack.addDelegate(Tags.effectDelegateTag, delegate)
                
        return attack
                
    @staticmethod
    def getDelegate(tree, delegateCategory, attack):
        """ Returns the delegate of the given category """
        delegate = tree.find(delegateCategory)
        if delegate:
            return AttackFactory.factories[delegateCategory].loadFromXML(delegate, attack)
        else:
            return AttackFactory.factories[delegateCategory].buildNull()