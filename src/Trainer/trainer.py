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
                
    def getAction(self, user, targets, screen):
        """ Get Trainer's action """
        if user.actionLock:
            action = user.actionLock.useAction()
        else:
            action = self.pickAction(user, targets, screen)
            
        return action
            
    def pickAction(self, user, targets, screen):
        """ Has the trainer pick its action via the screen
             Should be overwritten in subclasses """
        return AttackAction(None, None, None)
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ""
        