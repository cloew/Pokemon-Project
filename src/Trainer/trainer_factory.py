import xml.etree.ElementTree

from Pokemon.pokemon_factory import PokemonFactory
from resources.tags import Tags
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

class TrainerFactory:
    """ Builds a Trainer """
    HUMAN = 1
    COMPUTER = 2
    trainers = {HUMAN:HumanTrainer,
                   COMPUTER:ComputerTrainer}
                   
    @staticmethod
    def getPlayableTrainers():
        """ Returns a list of the playable trainers """
        playableTrainers = []
        
        tree = TrainerFactory.getTrainerdexTree()
        for trainerXML in tree.getiterator(Tags.trainerTag):
            if trainerXML.find(Tags.playableTag) != None:
                trainer = HumanTrainer() # May want to use the dict up top
                TrainerFactory.buildTrainerFromXML(trainer, trainerXML)
                playableTrainers.append(trainer)
        return  playableTrainers
    
    @staticmethod
    def loadFromXML(title, name, trainerType):
        """ Loads a Trainer from an XML file """
        tree = TrainerFactory.getTrainerdexTree()
        tree = TrainerFactory.getTrainerXML(tree, title, name)
        
        if tree == None:
            print "Could not find Trainer:", title, name
            return None
            
        trainer = TrainerFactory.buildTrainerFromType(trainerType)
        TrainerFactory.buildTrainerFromXML(trainer, tree)
        return trainer
        
    @staticmethod
    def buildTrainerFromType(type):
        """ Builds a Pokemon as a certain Trainer Type """
        return TrainerFactory.trainers[type]()
        
    @staticmethod
    def buildTrainerFromXML(trainer, tree):
        """ Builds a Trainer from XML """
        trainer.name = tree.find(Tags.nameTag).text
        trainer.title = tree.find(Tags.titleTag).text
        
        TrainerFactory.loadPokemonFromXML(trainer, tree)
        
    @staticmethod
    def loadPokemonFromXML(trainer, tree):
        """ Loads the Trainer's Pokemon from XML """
        pokemon = []
        tree = tree.find(Tags.beltTag)
        
        for pkmn in tree.getiterator(Tags.pokemonTag):
            pokemon.append(PokemonFactory.loadFromXML(pkmn))
        
        trainer.beltPokemon = pokemon
        
    @staticmethod
    def getTrainerdexTree():
        """ Opens the trainerdex.xml file as an element tree """
        try:
            trainerdex = open("resources/trainerdex.xml", 'r')
        except IOError:
            print "Unable to open TRAINERDEX"
            exit(-2)
    
        tree = xml.etree.ElementTree.ElementTree(file=trainerdex)
        trainerdex.close()
        return tree
        
    @staticmethod
    def getTrainerXML(tree, title, name):
        """ Returns the XML tree for the trainer with the name given """
        for trainer in tree.getiterator(Tags.trainerTag):
            if trainer.find(Tags.nameTag).text == name:
                if trainer.find(Tags.titleTag).text == title:
                    return trainer