import xml.etree.ElementTree

from statmodonstatus_ability import StatModOnStatusAbility

from resources.tags import Tags

class AbilityFactory:
    """ Builds Abilities """
    
    @staticmethod
    def loadFromPkmnXML(file):
        """ Load an attack as saved within a Pokemon instance in an XML file """
        # Get Ability XML
        name = file.readline().strip()
        tree = AbilityFactory.getAbilitydexTree()
        tree = AbilityFactory.getAbilityXML(tree, name)
        
        # Build the ABility
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
        
        if abilityType == "STAT MOD ON STATUS":
            status = tree.find(Tags.statusTag).text
            stat = tree.find(Tags.statTag).text
            mod = float(tree.find(Tags.degreeTag).text)
            return StatModOnStatusAbility(name, status, stat, mod)