from person import Person
from Zone.Person.Interaction.interaction_delegate import InteractionDelegate

from resources.tags import Tags

def LoadPeopleFromZoneXML(element, tiles, callback):
    """ Load a list of People form a Zone Element """
    people = []
    peopleElement = element.find(Tags.peopleTag)
    for personElement in peopleElement.findall(Tags.personTag):
        people.append(LoadPerson(personElement, tiles, callback))
    return people
    
def LoadPerson(element, tiles, callback):
    """ Load a Person from a Person XML Element """
    row, column = LoadPosition(element)
    tile = tiles[row][column]
    message = element.findtext(Tags.messageTag)
    imageFilename = element.findtext(Tags.imageTag)
    return Person(tile, imageFilename, InteractionDelegate(message, callback))
    
def LoadPosition(element):
    """ Loads a position and returns the row and column """
    positionElement = element.find(Tags.positionTag)
    row = int(positionElement.findtext(Tags.rowTag))
    column  = int(positionElement.findtext(Tags.columnTag))
    return row, column