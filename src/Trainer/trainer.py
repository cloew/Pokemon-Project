from Pokemon.pokemon_factory import PokemonFactory
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
            self.beltPokemon.append(PokemonFactory.loadFromTrainerFile(file))
        
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
                
    def choosePokemon(self):
        """ Returns a Pkmn chosen by the Trainer """
        return self.getPokemon(0)
                
    def hasMorePokemon(self):
        """ Returns whether the trainer has more Pokemon """
        for poke in self.beltPokemon:
            if not poke.isFainted():
                return True
                
        return False
                
    def getAction(self, user, targets):
        """ Get Trainer's action """
        if user.actionLock:
            action = user.actionLock.useAction()
        else:
            action = self.pickAction(user, targets)
            
        return action
            
    def pickAction(self, user, targets):
        """ Has the trainer pick its action via the screen
             Should be overwritten in subclasses """
        return AttackAction(None, None, None)
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ""
        
    def beaten(self):
        """ Returns a string that tells that the Trainer was beaten in Battle """