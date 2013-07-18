from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonStatsView:
    """ View for a Pokemon's Stats in a Battle """
    
    def __init__(self, pokemon):
        """ Initialize the Pokemon Stats View """
        self.pokemon = pokemon
        self.setPokemonMenuEntryView()
    
    def setPokemonMenuEntryView(self):
        """ Sets the Pokemon Menu Entry """
        menuEntry = PokemonMenuEntry(self.pokemon.pkmn, None)
        self.menuEntryView = MenuEntryView(menuEntry, None)
        
    def draw(self):
        """ Draw the Pokemon Stats View """
        return self.menuEntryView.draw()
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setPokemonMenuEntryView()