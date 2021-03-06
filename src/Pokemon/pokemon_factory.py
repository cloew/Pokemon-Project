import xml.etree.ElementTree

from Battle.Status.status import Status

from pokemon import Pokemon
from pokemon_battle_delegate_factory import PokemonBattleDelegateFactory
from Pokemon.Abilities.ability import Ability
from Pokemon.Abilities.abilityfactory import AbilityFactory
from Pokemon.DisplayDelegate.pokemon_display_delegate_factory import PokemonDisplayDelegateFactory
import Pokemon.Experience.experience_delegate_factory as ExperienceDelegateFactory
from Pokemon.Species.species_factory import SpeciesFactory

from resources.tags import Tags

import copy

class PokemonFactory:
    """ Factory to build Pokemon """
    
    @staticmethod
    def buildStarter(speciesName):
        """ Creates a Pokemon with Starter stats """
        name = speciesName
        species = SpeciesFactory.getSpecies(speciesName)
        level = 5
        pkmn = Pokemon(name, level, species)
        pkmn.id = ""
        
        pkmn.ability = Ability(None)
        pkmn.battleDelegate = PokemonBattleDelegateFactory.buildStarter(pkmn)
        pkmn.displayDelegate = PokemonDisplayDelegateFactory.buildStarter(species)
        # pkmn.experienceDelegate = ExperienceDelegateFactory.loadFromXML(pkmn, tree)
    
        return pkmn
    
    @staticmethod
    def loadFromXML(tree):
        """ Loads a Pokemon object from a file """
        name = tree.findtext(Tags.nameTag)
        speciesName = tree.findtext(Tags.speciesTag)
        species = SpeciesFactory.getSpecies(speciesName)
        level = int(tree.findtext(Tags.levelTag))
        
        pkmn = Pokemon(name, level, species)
        
        pkmn.id = ""
        
        pkmn.ability = AbilityFactory.loadFromPkmnXML(tree.find(Tags.abilityTag).text)
        pkmn.battleDelegate = PokemonBattleDelegateFactory.loadFromXML(pkmn, tree)
        pkmn.displayDelegate = PokemonDisplayDelegateFactory.loadFromXML(tree.find(Tags.displayTag), pkmn)
        pkmn.experienceDelegate = ExperienceDelegateFactory.loadFromXML(pkmn, tree)
    
        return pkmn
        
    @staticmethod
    def loadFromDB():
        """ AAAAAAAAAGGGGGGGGGGGHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! """
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        copiedPkmn = copy.deepcopy(toCopy)
        copiedPkmn.battleDelegate.attacks = toCopy.battleDelegate.attacks
        return copiedPkmn