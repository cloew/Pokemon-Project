
class Effectiveness:
    """ Used to get effectiveness of attacks based on TYPE """
    modByType = {"NORMAL":{"ROCK":.5, "GHOST":0, "STEEL":.5},
                 "FIRE":{"FIRE":.5, "WATER":.5, "GRASS":2, "ICE":2, "BUG":2, "ROCK":.5,
                             "DRAGON":.5, "STEEL":2},
                 "WATER":{"FIRE":2, "WATER":.5, "GRASS":.5, "GROUND":2,  "ROCK":2,
                              "DRAGON":.5},
                  "ELECTRIC":{"WATER":2, "ELECTRIC":.5, "GRASS":.5, "GROUND":0,
                              "FLYING":2, "DRAGON":.5},
                  "GRASS":{"FIRE":.5, "WATER":2, "GRASS":.5, "POISON":.5, "GROUND":2,
                                  "FLYING":.5, "BUG":.5, "ROCK":2, "DRAGON":.5, "STEEL":.5},
                  "ICE":{"FIRE":.5, "WATER":.5, "GRASS":2, "ICE":.5, "GROUND":2, 
                             "FLYING":2, "DRAGON":2, "STEEL":.5},
                  "FIGHTING":{"NORMAL":2, "ICE":2, "POISON":.5, "FLYING":.5, "PSYCHIC":.5,
                                      "BUG":.5, "ROCK":2, "GHOST":0, "DARK":2, "STEEL":2},
                  "POISON":{"GRASS":2, "POISON":.5, "GROUND":.5, "ROCK":.5, "GHOST":.5,
                                   "STEEL":0},
                  "GROUND":{"FIRE":2, "ELECTRIC":2, "GRASS":.5, "POISON":2, "FLYING":0,
                                     "BUG":.5, "ROCK":2, "STEEL":2},
                  "FLYING":{"ELECTRIC":.5, "GRASS":2, "FIGHTING":2, "BUG":2, "ROCK":.5,
                                  "STEEL":.5},
                  "PSYCHIC":{"FIGHTING":2, "POISON":2, "PSYCHIC":.5, "DARK":0, "STEEL":.5},
                  "BUG":{"FIRE":.5, "GRASS":2, "FIGHTING":.5, "POISON":.5, "FLYING":.5,
                              "PSYCHIC":2, "GHOST":.5, "DARK":2, "STEEL":.5},
                  "ROCK":{"FIRE":2, "ICE":2, "FIGHTING":.5, "GROUND":.5, "FLYING":2, "BUG":2,
                                "STEEL":.5},
                  "GHOST":{"NORMAL":0, "PSYCHIC":2, "GHOST":2, "DARK":.5, "STEEL":.5},
                  "DRAGON":{"DRAGON":2, "STEEL":.5},
                  "DARK":{"FIGHTING":.5, "PSYCHIC":2, "GHOST":2, "DARK":.5, "STEEL":.5},
                  "STEEL":{"FIRE":.5, "WATER":.5, "ELECTRIC":.5, "ICE":2, "ROCK":2, "STEEL":.5}
                  }
    immuneResponse = "It has no effect."
    ineffectiveResponse = "It wasn't very effective."
    effectiveResponse = None
    superEffectiveResponse = "It's super-effective."
                            
    def getMod(self, attackType, pokeType):
        """ Returns the modifier bonus of the Effectiveness of an attack against a Pokemon's Type """
        modForTypeDict = self.modByType[attackType]
        if pokeType in modForTypeDict:
            return modForTypeDict[pokeType]
        else:
            return 1
            
    def getEffectiveness(self, attackType, pokeTypes):
        """ Returns the effectiveness of an attack against a pokemon """
        mod = 1
        if not attackType == "":
            for type in pokeTypes:
                mod = mod*self.getMod(attackType, type)
            
        return mod, self.respond(mod)
    
    def respond(self, mod):
        """ Chooses the response message based on modifiers """
        if mod is 0:
            return self.immuneResponse
        elif mod is 1:
            return self.effectiveResponse
        elif mod < 1:
            return self.ineffectiveResponse
        elif mod > 1:
            return self.superEffectiveResponse
        