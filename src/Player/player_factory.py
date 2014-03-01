from Player.player import Player
from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from XML.xml_factory import XmlFactory

from xml.dom.minidom import parseString
from xml.etree.ElementTree import ElementTree, SubElement, tostring

factory = XmlFactory("player.xml")

class PlayerFactory(XmlFactory):
    """ Represents the Player Factory """
    
    def __init__(self):
        """ Initialize the player factory """
        XmlFactory.__init__(self, "player.xml")
        
    def createNewPlayer(self, name):
        """ Create a New Player """
        title = "Pokemon Trainer"
        player = Player(name)
        
        playerElement = SubElement(self.rootElement, Tags.playerTag)
        nameElement = SubElement(playerElement, Tags.nameTag)
        nameElement.text = player.name
        self.saveXMLTree()
        return player

PlayerFactory = PlayerFactory()