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
        
        self.setLastPlayer()
        
        playerElement = SubElement(self.rootElement, Tags.playerTag)
        trainerElement = SubElement(playerElement, Tags.trainerTag)
        nameElement = SubElement(trainerElement, Tags.nameTag)
        nameElement.text = trainer.name
        titleElement = SubElement(trainerElement, Tags.titleTag)
        titleElement.text = trainer.title
        lastPlayerElement = SubElement(playerElement, Tags.lastTag)
        lastPlayerElement.text = "true"
        self.saveXMLTree()
        return player
        
    def setLastPlayer(self):
        """ Set the Last Player field on all the players """
        for playerElement in self.tree.getiterator(Tags.playerTag):
            lastPlayerElement = playerElement.find(Tags.lastTag)
            lastPlayerElement.text = "false"
        self.saveXMLTree()
        
    def getLastPlayer(self):
        """ Return the last Player played as """
        playerElement = self.getLastPlayerElement()
        if playerElement is None:
            return None
        
        trainer = self.loadTrainerFromPlayerElement(playerElement)
        return Player(trainer)
        
    def getLastPlayerElement(self):
        """ Return the last Player played as """
        for playerElement in self.tree.getiterator(Tags.playerTag):
            if playerElement.findtext(Tags.lastTag) == "true":
                return playerElement
        
    def loadTrainerFromPlayerElement(self, playerElement):
        """ Load a trainer from a player element """
        trainerElement = playerElement.find(Tags.trainerTag)
        title = trainerElement.findtext(Tags.titleTag)
        name = trainerElement.findtext(Tags.nameTag)
        
        return TrainerFactory.loadFromXML(title, name, trainerType=TrainerFactory.HUMAN)

PlayerFactory = PlayerFactory()