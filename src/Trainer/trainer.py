from Pokemon.pokemon import Pokemon
from Battle.Actions.attack_action import AttackAction

import random

class Trainer:
    """ Represents a Pokemon Trainer """
    
    def __init__(self):
        self.actionLock = None
    
    def loadFromFile(self, file) :
        """ Loads a Trainer from a file """
        self.name = file.readline().strip()
        self.title = file.readline().strip()
        
        self.beltPokemon = []
        numPokemon = int(file.readline())
        for x in range(numPokemon):
            self.beltPokemon.append(Pokemon().loadFromHumanTrainerFile(file))
            
        #self.actionLock = None # Needs to be moved to PkmnBattleWrapper
        
        return self
        
    def announcePkmn(self, pkmn):
        """ Announces the Pokemon """
        
    def getPokemon(self, i):
        """ Returns the first Battle-ready Pokemon on the Belt 
        Skips fainted Pkmn and eggs '"""
        if i >= len(self.beltPokemon):
            return None
        
        for pkmn in self.beltPokemon[i:]:
            if not pkmn.isFainted():
                return pkmn
                
    def hasMorePokemon(self):
        """ Returns whether the trainer has more Pokemon """
        for poke in self.beltPokemon:
            if not poke.isFainted():
                return True
                
        return False
                
    # I'll prolly build a wrapper for this on the BattleSide to make it easier for multiple trainers on one side
    def getAction(self, currPokemon): 
        """ Get action, randomly pick an available attack """
        return None
        
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ""
        