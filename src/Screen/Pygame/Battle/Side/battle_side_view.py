from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface, load_image
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class BattleSideView:
    """ View for a battle side in a Pokemon Battle """
    
    def __init__(self, side):
        """ Initialize the Battle Side View """
        self.side = side
        self.setPokemonMenuEntryView()
        self.setPokemonImage()
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
    def update(self):
        """ Update the Battle Side View """
        self.setPokemonMenuEntryView()
        self.setPokemonImage()
        
    def getBackgroundSurface(self):
        """ Returns the Background surface """
        surface = GetTransparentSurface(self.width, self.height)
        return surface
        
    def setPokemonMenuEntryView(self):
        """ Sets the Pokemon Menu Entry """
        menuEntry = PokemonMenuEntry(self.side.pkmnInPlay[0].pkmn, None)
        self.menuEntryView = MenuEntryView(menuEntry, None)
        
    def setPokemonImage(self):
        """ Set the pokemon Image """
        self.pokemonImage = load_image("bulbasaur.png")