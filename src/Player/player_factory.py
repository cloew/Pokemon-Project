from Player.player import Player
from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from Trainer.trainer_factory import TrainerFactory
from XML.xml_factory import XmlFactory

from xml.dom.minidom import parseString
from xml.etree.ElementTree import SubElement

class PlayerFactory(XmlFactory):
    """ Represents the Player Factory """
    
    def __init__(self):
        """ Initialize the player factory """
        XmlFactory.__init__(self, "player.xml")
        
    def createNewPlayer(self, name):
        """ Create a New Player """
        trainer = TrainerFactory.createNewTrainer("Pokemon Trainer", name)
        player = Player(trainer)
        
        playerElement = SubElement(self.rootElement, Tags.playerTag)
        trainerElement = SubElement(playerElement, Tags.trainerTag)
        nameElement = SubElement(trainerElement, Tags.nameTag)
        nameElement.text = trainer.name
        titleElement = SubElement(trainerElement, Tags.titleTag)
        titleElement.text = trainer.title
        self.saveXMLTree()
        return player

PlayerFactory = PlayerFactory()