from Player.player import Player
from resources.tags import Tags

from xml.dom.minidom import parseString
from xml.etree.ElementTree import SubElement, tostring

tree = None

def NewPlayer(name):
    """ Create a new player from the given name """
    player = Player(player)
    
    tree = GetXMLTree()
    playerElement = SubElement(tree.getroot(), Tags.playerTag)
    nameElement = SubElement(playerElement, Tags.nameTag)
    nameElement.text = player.name
    SaveXMLTree(tree)
    
def GetXMLTree():
    """ Return the Player XML Tree """
    global tree
    
    if tree is None:
        with open(GetResourcePath("player.xml"), 'r') as playerTreeFile:
            tree = xml.etree.ElementTree.ElementTree(file=playerTreeFile)
    return tree
    
def SaveXMLTree(tree):
    """ Save the Player XML Tree """
    xmlString = tostring(tree.getroot())
    
    xmlString = xmlString.replace('\n', '')
    xmlString = xmlString.replace('\t', '')
    xmlString = xmlString.replace('ns0:', '')
    xmlString = xmlString.replace(':ns0', '')
    
    xml = parseString(xmlString)
    prettyXMLString = xml.toprettyxml()
    
    with open(GetResourcePath("player.xml"), 'w') as file:
        file.write(prettyXMLString)