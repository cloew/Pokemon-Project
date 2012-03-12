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
        pkmn.ability = Ability()
        pkmn.battleDelegate = PokemonBattleDelegateFactory.buildStarter(pkmn)
    
        return pkmn
    
    @staticmethod
    def loadFromTrainerFile(file):
        """ Loads a Pokemon object from a file """
        pkmn = Pokemon()
        
        values = file.readline().strip().split(" ")
        pkmn.name = values[0]
        pkmn.species = values[1]
        pkmn.level = int(values[2])
    
        pkmn.id = ""
        pkmn.ability = AbilityFactory.loadFromPkmnXML(file)
        pkmn.battleDelegate = PokemonBattleDelegateFactory.loadFromTrainerFile(pkmn, file)
    
        return pkmn
                
    