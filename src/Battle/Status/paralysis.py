from Battle.Status.status import Status

import random

class Paralysis(Status):
    """ Represents the status of paralysis """
    abbr = "PAR"
    threshold = 25 # % chance to be paralyzed
    start = " is paralyzed. It may be unable to move."
    cantMove = " is paralyzed. It can't move."
    done = " is paralyzed no more."
    
    def __init__(self):
        """ Build a paralysis status """
        self.initialize()
        self.statMods["SPD"] = .25
        
    def immobilized(self, pkmn):
        """ Return whether the user is paralyzed
        and any messages for the screen"""
        if Paralysis.paralyzed(random.randint(0, 99)):
            return True, [pkmn.getHeader() + Paralysis.cantMove]
        return False, []
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types is immune to the status """
        return "GROUND" in targetTypes and attackType == "ELECTRIC"
     
    @staticmethod
    def paralyzed(rand):
        """ Uses rand to determine if the user is paralyzed """
        return rand < Paralysis.threshold