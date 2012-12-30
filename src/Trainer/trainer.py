from Pokemon.pokemon_factory import PokemonFactory
from Battle.Actions.attack_action import AttackAction

import random

class Trainer:
    """ Represents a Pokemon Trainer """
    
    def __init__(self):
        self.actionLock = None
        
    def getPokemon(self, i):
        """ Returns the first Battle-ready Pokemon on the Belt 
        Skips fainted Pkmn and eggs '"""
        if i >= len(self.beltPokemon):
            return None
        
        for pkmn in self.beltPokemon[i:]:
            if not pkmn.fainted():
                return pkmn
                
    def choosePokemon(self, pkmnInPlay):
        """ Returns a Pkmn chosen by the Trainer """
        return self.chooseRandomPokemon(pkmnInPlay)
        
    def chooseRandomPokemon(self, pkmnInPlay):
        """ Chooses a Random Pokemon """
        pkmnOut = []
        for pkmn in pkmnInPlay:
            pkmnOut.append(pkmn.pkmn)
        
        pkmn = None
        while pkmn in pkmnOut or pkmn is None or pkmn.fainted():
            pkmn = random.choice(self.beltPokemon)
            
        return pkmn
                
    def hasPokemon(self):
        """ Returns whether the trainer has Battle-Ready Pokemon Pokemon """
        for poke in self.beltPokemon:
            if not poke.fainted():
                return True
        return False
        
    def hasMorePokemon(self, pkmnInPlay):
        """ Returns whether the trainer has more Battle Ready Pokemon on its belt """
        pkmnOut = []
        for pkmn in pkmnInPlay:
            pkmnOut.append(pkmn.pkmn)
        
        for poke in self.beltPokemon:
            if not poke.fainted() and not poke in pkmnOut:
                return True
        return False
                
    def getAction(self, user, targets, playerSide, oppSide, environment):
        """ Get Trainer's action """
        if user.actionLock:
            action = user.actionLock.useAction()
        else:
            action = self.pickAction(user, targets, playerSide, oppSide, environment)
            
        return action
            
    def pickAction(self, user, targets, playerSide, oppSide, environment):
        """ Has the trainer pick its action via the screen
             Should be overwritten in subclasses """
        return AttackAction(None, None, None, None)
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ""
        
    def beaten(self):
        """ Returns a string that tells that the Trainer was beaten in Battle """