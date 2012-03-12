import xml.etree.ElementTree

from Battle.Attack.attackfactory import AttackFactory
from Battle.Status.status import Status

from pokemon_battle_delegate import PokemonBattleDelegate
from resources.tags import Tags

class PokemonBattleDelegateFactory:
    """ Factory to build Pokemon """
    
    statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]
    
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
        delegate.currHP = int(tree.find(Tags.currHPTag).text)
    
        # Read attacks
        delegate.attacks = []
        attacksTree = tree.find(Tags.attacksTag)
        for attack in attacksTree.getiterator(Tags.attackTag):
             delegate.attacks.append(AttackFactory.loadFromPkmnXML(attack))
        
        # Status
        delegate.status = Status()

        return delegate
    
    @staticmethod
    def loadPokedexBattleInfo(delegate, species):
        """ Gets info from Pokedex relevanty to Battling
        Types, base stats """
        # Open Pokedex and set variables that require Pokedex data
        tree = PokemonBattleDelegateFactory.getPokedexTree()
        tree = PokemonBattleDelegateFactory.getPkmnXML(tree, species)

        # Get type(s) -- Prolly should be its own fuunction
        typesTree = tree.find(Tags.typesTag)
        types = []
        for type in typesTree.getiterator(Tags.typeTag):
            types.append(type.text)
        delegate.types = types
    
        # Get stats -- Prolly should be its own function
        delegate.stats = {}
        statsTree = tree.find(Tags.baseStatsTag)
        for key in PokemonBattleDelegateFactory.statKeys:
            baseStat = int(statsTree.find(key).text)
            if (key is "HP"):
                # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level
                delegate.stats[key] = int(((2*int(baseStat))*delegate.parent.level/100.0)+10 + delegate.parent.level )
            else:
                # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
                delegate.stats[key] = int(((2*int(baseStat))* delegate.parent.level/100.0) + 5)
                
    @staticmethod
    def getPokedexTree():
        """ Opens the pokedex.xml file as an element tree """
        try:
            pokedex = open("resources/pokedex.xml", 'r')
        except IOError:
            print "Unable to open POKEDEX"
            exit(-2)
    
        tree = xml.etree.ElementTree.ElementTree(file=pokedex)
        pokedex.close()
        return tree
        
    @staticmethod
    def getPkmnXML(tree, species):
        """ Returns the XML tree for the pokemon with the species given """
        for pkmn in tree.getiterator(Tags.pokemonTag):
            if pkmn.find(Tags.speciesTag).text == species:
                return pkmn