from Pokemon.Abilities.abilityfactory import AbilityFactory
from Pokemon.Abilities.ability import Ability
from Pokemon.pokemon_battle_delegate import PokemonBattleDelegate

import sys

class Pokemon:
    """ Holds the information for a Pokemon """
  
    def __init__(self, species=None):
        """ Builds a Pkmn """
        if species:
            self.buildStarter(species)
        
    def buildStarter(self, species):
        """ Creates a Pokemon with Starter stats """
        self.name = species
        self.species = species
        self.level = 5
        self.ability = Ability()
        self.battleDelegate = PokemonBattleDelegate().buildStarter(self)
        
  
    def loadFromHumanTrainerFile(self, file):
        """ Loads a Pokemon object from a file """
        values = file.readline().strip().split(" ")
        self.name = values[0]
        self.species = values[1]
        self.level = int(values[2])
    
        self.id = ""
        self.ability = AbilityFactory.loadFromPkmnXML(file)
        self.battleDelegate = PokemonBattleDelegate().loadFromHumanTrainerFile(self, file)
    
        return self
    
    def getAttacks(self):
        """ Returns the Pokemon's Attacks """
        return self.battleDelegate.attacks

    def isFainted(self):
        """ Returns if the Pkmn is fainted or not """
        return self.battleDelegate.currHP is 0
        
    def takeDamage(self, damage):
        """ Has the Pokemon take damage """
        self.battleDelegate.takeDamage(damage)
        
    def heal(self, heal):
        """ Has the Pokemon heal itself """
        self.battleDelegate.heal(heal)
        
    def getStat(self, stat):
        """ Returns the given Stat """
        return self.battleDelegate.stats[stat]*self.battleDelegate.status.getStatMod(stat)
        
    def setStat(self, stat, amount):
        """ Set the given Stat to the given Amount """
        self.battleDelegate.stats[stat] = amount
        
    def getCurrHP(self):
        """ Return the Pokemon's Current HP """
        return self.battleDelegate.currHP
        
    def setCurrHP(self, amount):
        """ Sets the Pokemon's Current HP to the given amount """
        self.battleDelegate.currHP = amount
        
    def getStatus(self):
        """ Gets the status of the Pokemon """
        return self.battleDelegate.status
        
    def setStatus(self, status):
        """ Sets the status of the Pokemon """
        self.battleDelegate.status = status
        
    def getTypes(self):
        """ Returns the Pokemon's types """
        return self.battleDelegate.types
        
    def getRatioOfHealth(self, ratio):
        """ Returns the ratio of the pokemon's health """
        val = int(self.getStat("HP")/float(ratio))
        if val == 0:
            return 1
        return val