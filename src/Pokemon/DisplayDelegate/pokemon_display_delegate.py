
class PokemonDisplayDelegate:
    """ Delegate for special ways a Pokemon can be displayed """
    
    def __init__(self, species):
        """ Initialize the Pokemon Display Delegate """
        self.species = species
        
    def getDisplayImageBaseName(self):
        """ Return the Base Image Name based on the species """
        return self.species.name.lower()