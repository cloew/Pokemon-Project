from resources.resource_manager import GetResourcePath
from resources.tags import Tags

import xml.etree.ElementTree

tree = None

def loadSpeciesXML(species):
    """ Returns the XML tree for the pokemon with the species given """
    tree = getPokedexTree()
    
    for pkmn in tree.getiterator(Tags.pokemonTag):
        if pkmn.find(Tags.speciesTag).text == species:
            return pkmn

def getPokedexTree():
    """ Opens the pokedex.xml file as an element tree """
    global tree
    if tree is not None:
        return tree
        
    try:
        with open(GetResourcePath("pokedex.xml"), 'r') as pokedex:
            tree = xml.etree.ElementTree.ElementTree(file=pokedex)
    except IOError:
        print "Unable to open POKEDEX"
        exit(-2)

    return tree