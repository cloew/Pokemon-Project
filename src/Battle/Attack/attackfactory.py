import xml.etree.ElementTree

from Battle.Attack.attack import Attack

from Battle.Attack.DamageDelegates.damage_delegatefactory import DamageDelegateFactory
from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory
from Battle.Attack.HitDelegates.hit_delegatefactory import HitDelegateFactory
from Battle.Attack.SpeedDelegates.speed_delegatefactory import SpeedDelegateFactory
from Battle.Attack.CritDelegates.crit_delegatefactory import CritDelegateFactory

from resources.tags import Tags
from resources.sqlite.pokemon_sqlite_helper import PkmnDBConnect

class AttackFactory:
    """ Builds an Attack, includng Delegates """
    tree = None
    factories = {Tags.hitDelegateTag:HitDelegateFactory,
                      Tags.damageDelegateTag:DamageDelegateFactory,
                      Tags.speedDelegateTag:SpeedDelegateFactory,
                      Tags.critDelegateTag:CritDelegateFactory}
    
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
    def loadFromPkmnXML(tree):
        """ Load an attack as saved within a Pokemon instance in an XML file """
        # Get Attack XML
        name = tree.find(Tags.nameTag).text
        attack = AttackFactory.loadFromXML(name)
    
        # Get currPP and PP from file
        attack.powerPoints = int(tree.find(Tags.ppTag).text)
        attack.currPowerPoints = int(tree.find(Tags.currPPTag).text)
    
        return attack
        
    @staticmethod
    def getAttackAsNew(name):
        """ Build an attack entirely from attackdex """
        # Build the Attack
        tree = AttackFactory.getAttackdexTree()
        tree = AttackFactory.getAttackXML(tree, name)
        attack = AttackFactory.buildAttackFromXML(tree)
    
        # Get currPP and PP from attackdex
        attack.powerPoints = int(tree.find(Tags.ppTag).text)
        attack.currPowerPoints = attack.powerPoints
    
        return attack
        
    @staticmethod
    def loadFromXML(name):
        """ Loads an Attack from Attackdex XML """
        tree = AttackFactory.getAttackdexTree()
        tree = AttackFactory.getAttackXML(tree, name)
        
        # Build the Attack
        return AttackFactory.buildAttackFromXML(tree)
        
    @staticmethod
    def loadFromDB(name):
        """ Loads an attack from a Database """
        connection = PkmnDBConnect()
        cursor = connection.cursor()
        
        attack = AttackFactory.buildAttackFromDB(cursor, name)
        connection.close()
        return attack
        
    @staticmethod
    def getAttackdexTree():
        """ Opens the attackdex.xml file as an element tree """
        if AttackFactory.tree is not None:
            return AttackFactory.tree
        
        try:
            attackdex = open("resources/attackdex.xml", 'r')
        except IOError:
            print "Unable to open ATTACKDEX"
            exit(-2)
    
        AttackFactory.tree = xml.etree.ElementTree.ElementTree(file=attackdex)
        attackdex.close()
        return AttackFactory.tree
        
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
    def buildAttackFromDB(cursor, name):
        """ Build an Attack from a Database connection """
        attack = Attack()
        
        cursor.execute("SELECT Type.name from Attack, Type where Attack.name = ? and Attack.type_id = Type.id", (name,))
        type = cursor.fetchone()[0]
        
        attack.name = name
        attack.type = type
        
        # Delegates
        for delegateCategory in AttackFactory.factories.keys():
            delegate = AttackFactory.getDelegateDB(cursor, delegateCategory, attack)
            attack.addDelegate(delegateCategory, delegate)
            
        attack.effectDelegates = EffectDelegateFactory.loadAllEffectsFromDB(cursor, attack)
                
        return attack
                
    @staticmethod
    def getDelegate(tree, delegateCategory, attack):
        """ Returns the delegate of the given category """
        delegate = tree.find(delegateCategory)
        if delegate:
            return AttackFactory.factories[delegateCategory].loadFromXML(delegate, attack)
        else:
            return AttackFactory.factories[delegateCategory].buildNull()
            
    @staticmethod
    def getDelegateDB(cursor, delegateCategory, attack):
        """ Returns the delegate of the given category """
        delegate = AttackFactory.factories[delegateCategory].loadFromDB(cursor, attack)
        if delegate is None:
            delegate = AttackFactory.factories[delegateCategory].buildNull()
        return delegate