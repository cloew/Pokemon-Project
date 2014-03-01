from Pokemon.pokemon_factory import PokemonFactory

from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

from XML.xml_factory import XmlFactory
from xml.etree.ElementTree import SubElement

class TrainerFactory(XmlFactory):
    """ Builds a Trainer """
    HUMAN = 1
    COMPUTER = 2
    trainers = {HUMAN:HumanTrainer,
                COMPUTER:ComputerTrainer}
                
    def __init__(self):
        """ Initialize the Trainer Factory """
        XmlFactory.__init__(self, "trainerdex.xml")
                   
    def getPlayableTrainers(self):
        """ Returns a list of the playable trainers """
        playableTrainers = []
        
        # tree = TrainerFactory.getTrainerdexTree()
        for trainerXML in self.tree.getiterator(Tags.trainerTag):
            if trainerXML.find(Tags.playableTag) != None:
                trainer = HumanTrainer() # May want to use the dict up top
                self.buildTrainerFromXML(trainer, trainerXML) # Really slow for whatever reason
                playableTrainers.append(trainer)
        
        return  playableTrainers
    
    def loadFromXML(self, title, name, trainerType=COMPUTER):
        """ Loads a Trainer from an XML file """
        tree = self.getTrainerXML(title, name)
        
        if tree == None:
            print "Could not find Trainer:", title, name
            return None
            
        trainer = self.buildTrainerFromType(trainerType)
        self.buildTrainerFromXML(trainer, tree)
        return trainer
        
    def buildTrainerFromType(self, type):
        """ Builds a Pokemon as a certain Trainer Type """
        return TrainerFactory.trainers[type]()
        
    def buildTrainerFromXML(self, trainer, tree):
        """ Builds a Trainer from XML """
        trainer.name = tree.find(Tags.nameTag).text
        trainer.title = tree.find(Tags.titleTag).text
        
        TrainerFactory.loadPokemonFromXML(trainer, tree)
        
    def loadPokemonFromXML(self, trainer, tree):
        """ Loads the Trainer's Pokemon from XML """
        pokemon = []
        tree = tree.find(Tags.beltTag)
        
        for pkmn in tree.getiterator(Tags.pokemonTag):
            pokemon.append(PokemonFactory.loadFromXML(pkmn))
        
        trainer.beltPokemon = pokemon
        
    def getTrainerXML(self, title, name):
        """ Returns the XML Element for the trainer with the name given """
        for trainer in self.tree.getiterator(Tags.trainerTag):
            if trainer.find(Tags.nameTag).text == name:
                if trainer.find(Tags.titleTag).text == title:
                    return trainer
                    
    def createNewTrainer(self, title, name):
        """ Create a New Trainer """
        trainerElement = SubElement(self.rootElement, Tags.trainerTag)
        nameElement = SubElement(trainerElement, Tags.nameTag)
        nameElement.text = name
        titleElement = SubElement(trainerElement, Tags.titleTag)
        titleElement.text = title
                    
        trainer = self.buildTrainerFromType(self.HUMAN)
        trainer.title = title
        trainer.name = name
        return trainer

TrainerFactory = TrainerFactory()