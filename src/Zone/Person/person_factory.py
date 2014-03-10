from Trainer.trainer_factory import TrainerFactory

from Zone.Person.person import Person
from Zone.Person.trainer_person import TrainerPerson
from Zone.Person.Interaction.interaction_delegate import PersonInteractionDelegate

from resources.tags import Tags

def LoadPeopleFromZoneXML(element, tiles):
    """ Load a list of People form a Zone Element """
    people = []
    peopleElement = element.find(Tags.peopleTag)
    for personElement in peopleElement.findall(Tags.personTag):
        people.append(LoadPerson(personElement, tiles))
    return people
    
def LoadPerson(element, tiles):
    """ Load a Person from a Person XML Element """
    row, column = LoadPosition(element)
    tile = tiles[row][column]
    message = element.findtext(Tags.messageTag)
    imageFilename = element.findtext(Tags.imageTag)
    if element.find(Tags.trainerTag) is not None:
        trainer = LoadTrainer(element)
        return TrainerPerson(tile, imageFilename, trainer, PersonInteractionDelegate(message))
    else:
        return Person(tile, imageFilename, PersonInteractionDelegate(message))
        
def LoadTrainer(element):
    """ Load trainer from a Person Element """
    trainerElement = element.find(Tags.trainerTag)
    title = trainerElement.findtext(Tags.titleTag)
    name = trainerElement.findtext(Tags.nameTag)
    return TrainerFactory.loadFromXML(title, name, TrainerFactory.COMPUTER)
    
def LoadPosition(element):
    """ Loads a position and returns the row and column """
    positionElement = element.find(Tags.positionTag)
    row = int(positionElement.findtext(Tags.rowTag))
    column  = int(positionElement.findtext(Tags.columnTag))
    return row, column