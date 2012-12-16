from Menu.menu_entry import MenuEntry

class PokemonMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, pokemon, callback):
        """ Builds a pokemon menu entry with its pokemon """
        self.pokemon = pokemon
        MenuEntry.__init__(self, callback)
        
    def getPokemon(self):
        """ Returns the entry's pokemon """
        return self.pokemon
        
    def getTextLength(self):
        """ Return the printable length of the Entry's Text """
        return len(self.pokemon.name)

    def getText(self):
        """ Return text to display for the Entry """
        return self.pokemon.name
        