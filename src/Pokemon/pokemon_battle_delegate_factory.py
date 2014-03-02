from Battle.Attack.attackfactory import AttackFactory
from Battle.Status.status import Status

from pokemon_battle_delegate import PokemonBattleDelegate
from Pokemon.Species.species_factory import SpeciesFactory

from resources.resource_manager import GetResourcePath
from resources.tags import Tags

class PokemonBattleDelegateFactory:
    """ Factory to build Pokemon """
    
    statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]
    tree = None
    
    @staticmethod
    def buildStarter(parent):
        """ Builds a BattleDelegate for a Starter Pokemon """
        delegate = PokemonBattleDelegate()
        
        # Set parent
        delegate.parent = parent
    
        # Get common info from Pokedex 
        PokemonBattleDelegateFactory.loadPokedexBattleInfo(delegate, parent.species)
    
        # Set currHP to full
        delegate.currHP = delegate.stats["HP"]
    
        # Load attacks
        delegate.attacks = []
        
        # Status
        delegate.status = Status()
    
        return delegate
    
    @staticmethod
    def loadFromXML(parent, tree):
        """  Build a Pokemon's Battle Information """
        delegate = PokemonBattleDelegate()
        
        # Set parent
        delegate.parent = parent
    
        # Get Pokedex battle info on the Pokemon
        PokemonBattleDelegateFactory.loadPokedexBattleInfo(delegate, parent.species)
    
        # Get current HP
        delegate.parent.stats.currentHP = int(tree.find(Tags.currHPTag).text)
    
        # Read attacks
        delegate.attacks = []
        attacksTree = tree.find(Tags.attacksTag)
        for attack in attacksTree.getiterator(Tags.attackTag):
             delegate.attacks.append(AttackFactory.loadFromPkmnXML(attack))
        
        # Status
        delegate.status = Status()

        return delegate
        
    @staticmethod
    def copy(parent, toCopy):
        """ Creates a copy of the given Battle Delegate """
        delegate = PokemonBattleDelegate()
        
        delegate.parent = parent
        delegate.currHP = toCopy.currHP
        delegate.attacks = toCopy.attacks
        delegate.status = toCopy.status
        
        delegate.types = list(toCopy.types)
        delegate.stats = dict(toCopy.stats)
        
        return delegate
    
    @staticmethod
    def loadPokedexBattleInfo(delegate, species):
        """ Gets info from Pokedex relevant to Battling
        Types, base stats """
        # Open Pokedex and set variables that require Pokedex data
        tree = SpeciesFactory.loadSpeciesXML(species)

        # Get type(s) -- Prolly should be its own function
        typesTree = tree.find(Tags.typesTag)
        types = []
        for type in typesTree.getiterator(Tags.typeTag):
            types.append(type.text)
        delegate.types = types