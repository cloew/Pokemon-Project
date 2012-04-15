import sys
import xml.etree.ElementTree

import time

from resources.tags import Tags
from resources.sqlite.db_add_ability import DBAddAbility
from resources.sqlite.db_add_attack import DBAddAttack

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

def addAttacksFromXML():
    """  """
    front = DBAddAttack()
    tree = getAttackdexTree()
    for attack in tree.getiterator(Tags.attackTag):
        try:
            
            s = buildAttackString(attack)
            params = s.split('@')[1:]
            front.execute(params, close=False)
        except Exception as e:
            print e
        print ""
    front.connection.close()
    print "Done!!!"
    
def addAbilitiesFromXML():
    """  """
    front = DBAddAbility()
    tree = getAbilitydexTree()
    for attack in tree.getiterator(Tags.abilityTag):
        try:
            
            s = buildAbilityString(attack)
            params = s.split('@')[1:]
            front.execute(params, close=False)
        except Exception as e:
            print e
        print ""
    front.connection.close()
    print "Done!!!"
    
def buildAttackString(tree):
    """  """
    s = ""
    s += getParameterString(tree)
    s += getHitDelegate(tree.find(Tags.hitDelegateTag))
    s += getDamageDelegate(tree.find(Tags.damageDelegateTag))
    s += getCritDelegate(tree.find(Tags.critDelegateTag))
    s += getSpeedDelegate(tree.find(Tags.speedDelegateTag))
    s += getEffectDelegates(tree.find(Tags.effectDelegatesTag))
    
    return s
    
def buildAbilityString(tree):
    """  """
    s = ""
    s += getAbilityParameterString(tree)
    s += getAbility(tree)
    
    return s
    
def getAbilityParameterString(tree):
    """  """
    name = tree.find(Tags.nameTag).text.strip()
    return " @p %s" % (name,)
    
def getAbility(tree):
    """  """
    if tree is None:
        return ""
    
    s = ""
    for i in tree.getchildren()[1:]:
    
        if i.text.strip() == "":
            temp = ""
            for effect in i.getchildren():
                t= getInternalEffect(effect)
                if not t == "":
                    temp += t
                
            s += temp + ":" 
        else:
            s += i.text.strip() + ":"
    
    if s == "":
        return s
        
    return " @a %s" % s
    
def getParameterString(tree):
    """  """
    name = tree.find(Tags.nameTag).text.strip()
    type = tree.find(Tags.typeTag).text.strip()
    return " @p %s:%s" % (name, type)
    
def getHitDelegate(tree):
    """  """
    s = ""
    
    for i in tree.getiterator()[1:]:
        s += i.text.strip() + ":"
    return " @h %s" % s
    
def getDamageDelegate(tree):
    """  """
    if tree is None:
        return ""
    
    s = ""
    
    for i in tree.getiterator()[1:]:
        s += i.text.strip() + ":"
    return " @d %s" % s
    
def getCritDelegate(tree):
    """  """
    if tree is None:
        return " @c CORE:0"
    
    s = ""
    
    for i in tree.getiterator()[1:]:
        s += i.text.strip() + ":"
    return " @c %s" % s
    
def getSpeedDelegate(tree):
    """  """
    if tree is None:
        return " @s CORE:0"
    
    s = ""
    
    for i in tree.getchildren():
        s += i.text.strip() + ":"
    return " @s %s" % s
    
def getEffectDelegates(tree):
    """  """
    if tree is None:
        return ""
    
    s = ""
    for i in tree.getchildren():
        if i.tag == Tags.effectDelegateTag:
            s += getEffectDelegate(i)
        
        
    return s

def getEffectDelegate(tree):
    """  """
    if tree is None:
        return ""
    
    s = ""
    n = 0
    
    for i in tree.getchildren():
    
        if i.text.strip() == "":
            temp = ""
            for effect in i.getchildren():
                t= getInternalEffect(effect)
                if not t == "":
                    temp += t
                
            s += temp + ":" 
        else:
            s += i.text.strip() + ":"
    
    if s == "":
        return s
        
    return " @e %s" % s
    
def getInternalEffect(tree):
    """  """
    s = ""
    for i in tree.getchildren():
        s += i.text.strip() + "%"
        
    if s == "":
        return s
        
    return "_e %s" % s
    
def main(argv):
    """ Start the game """
    if argv[0] == "ATTACK":
        addAttacksFromXML()
    elif argv[0] == "ABILITY":
        addAbilitiesFromXML()

if __name__ == "__main__":
    main(sys.argv[1:])