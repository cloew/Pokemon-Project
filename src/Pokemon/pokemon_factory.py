import xml.etree.ElementTree

from Battle.Status.status import Status

from pokemon import Pokemon
from pokemon_battle_delegate_factory import PokemonBattleDelegateFactory
from Pokemon.Abilities.ability import Ability
from Pokemon.Abilities.abilityfactory import AbilityFactory

from resources.tags import Tags

class PokemonFactory:
    """ Factory to build Pokemon """
    
    @staticmethod
    def buildStarter(species):
        """ Creates a Pokemon with Starter stats """
        pkmn = Pokemon()
        
        pkmn.name = species
        pkmn.species = species
        pkmn.level = 5
        pkmn.id = ""
        
        pkmn.ability = Ability()
        pkmn.battleDelegate = PokemonBattleDelegateFactory.buildStarter(pkmn)
    
        return pkmn
    
    @staticmethod
    def loadFromXML(tree):
        """ Loads a Pokemon object from a file """
        pkmn = Pokemon()
        
        pkmn.name = tree.find(Tags.nameTag).text
        pkmn.species = tree.find(Tags.speciesTag).text
        pkmn.level = int(tree.find(Tags.levelTag).text)
        pkmn.id = ""
        
        pkmn.ability = AbilityFactory.loadFromPkmnXML(tree.find(Tags.abilityTag).text)
        pkmn.battleDelegate = PokemonBattleDelegateFactory.loadFromXML(pkmn, tree)
    
        return pkmn
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        pkmn = Pokemon()
        pkmn.name = str(toCopy.name)
        pkmn.species = str(toCopy.species)
        pkmn.level = toCopy.level
        pkmn.id = toCopy.id
        
        pkmn.ability = toCopy.ability
        pkmn.battleDelegate =PokemonBattleDelegateFactory.copy(pkmn, toCopy.battleDelegate)
        
        return pkmn