from Menu.text_menu_entry import TextMenuEntry
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonStatsView:
    """ View for a Pokemon's Stats in a Battle """
    
    def __init__(self, pokemon):
        """ Initialize the Pokemon Stats View """
        self.pokemon = pokemon
        self.setPokemonMenuEntryView()
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
    
    def setPokemonMenuEntryView(self):
        """ Sets the Pokemon Menu Entry """
        menuEntry = PokemonMenuEntry(self.getPokemon(), None)
        self.pkmnEntryView = MenuEntryView(menuEntry)
        self.setLevelMenuEntryView()
        
    def setLevelMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("Lv. {0}".format(self.pokemon.getLevel()), None)
        self.levelEntryView = MenuEntryView(menuEntry)
        
    def draw(self):
        """ Draw the Pokemon Stats View """
        surface = GetTransparentSurface(self.width, self.height)
        
        pkmnSurface = self.pkmnEntryView.draw()
        surface.blit(pkmnSurface, (0,0))
        
        levelSurface = self.levelEntryView.draw()
        levelSurfacePosition = levelSurface.get_rect(right=self.width, top=0)
        surface.blit(levelSurface, levelSurfacePosition)
        
        return surface
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setPokemonMenuEntryView()
        
    def getPokemon(self):
        """ Return the pokemon """
        return self.pokemon.pkmn