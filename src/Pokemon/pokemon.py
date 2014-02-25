from Pokemon.Abilities.abilityfactory import AbilityFactory
from Pokemon.Abilities.ability import Ability
from Pokemon.pokemon_battle_delegate import PokemonBattleDelegate
from Pokemon.DisplayDelegate.pokemon_display_delegate import PokemonDisplayDelegate
from Pokemon.Stats.stats import Stats

import sys

class Pokemon:
    """ Holds the information for a Pokemon """
  
    def __init__(self, name, level, species):
        """ Builds a Pkmn """
        self.name = name
        self.level = level
        self.species = species
        self.stats = Stats(self)
        
    def buildStarter(self, species):
        """ Creates a Pokemon with Starter stats """
        self.name = species
        self.species = species
        self.level = 5
        self.ability = Ability()
        self.battleDelegate = PokemonBattleDelegate().buildStarter(self)
        self.displayDelegate = PokemonDisplayDelegate(self.species)
    
        return self
        
    def getLevel(self):
        """ Return the level """
        return self.level
    
    def getAttacks(self):
        """ Returns the Pokemon's Attacks """
        return self.battleDelegate.attacks

    def fainted(self):
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
        
    def setTypes(self, types):
        """ Returns the Pokemon's types """
        self.battleDelegate.types = types
        
    def getRatioOfHealth(self, ratio, forDamage = False):
        """ Returns the ratio of the pokemon's health """
        val = int(self.getStat("HP")/float(ratio))
        if forDamage and val > self.getCurrHP():   # Need to revisit this
            return self.getCurrHP()
        elif val == 0:
            return 1
        return val
        
    def getDisplayImageBaseName(self):
        """ Return the Display Base Name """
        return self.displayDelegate.getDisplayImageBaseName()
        
    @property
    def experienceToAward(self):
        """ Return the experince to the next level """
        return self.experienceDelegate.experienceToAward
        
    def gainExperience(self, experience):
        """ Gain experience """
        self.experienceDelegate.gainExperience(experience)
        
    def canLevelUp(self):
        """ Return if the Pokemon has enough experience to level """
        return self.experienceDelegate.canLevelUp()
        
    def levelUp(self):
        """ Level up the Pokemon """
        self.level += 1