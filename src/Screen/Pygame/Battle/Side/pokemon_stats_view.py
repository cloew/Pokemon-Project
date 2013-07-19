from Menu.text_menu_entry import TextMenuEntry
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.HealthBar.health_bar_view import HealthBarView
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonStatsView:
    """ View for a Pokemon's Stats in a Battle """
    FONT_SIZE = 24
    
    def __init__(self, pokemon=None, pokemonMenuEntry=None):
        """ Initialize the Pokemon Stats View """
        if pokemon is not None:
            self.pokemon = pokemon
        else:
            self.pokemon = pokemonMenuEntry.getPokemon()
        self.setPokemonMenuEntryView(pokemonMenuEntry)
        self.healthBarView = HealthBarView(self.pokemon)
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
        self.healthBarView.setSize(self.width, self.height*.1)
    
    def setPokemonMenuEntryView(self, pokemonMenuEntry):
        """ Sets the Pokemon Menu Entry """
        if pokemonMenuEntry is None:
            pokemonMenuEntry = PokemonMenuEntry(self.pokemon, None)
        self.pkmnEntryView = MenuEntryView(pokemonMenuEntry, self.FONT_SIZE)
        self.setLevelMenuEntryView()
        self.setHealthMenuEntryView()
        
    def setLevelMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("Lv. {0}".format(self.pokemon.getLevel()), None)
        self.levelEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        
    def setHealthMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("{0}/{1}".format(self.pokemon.getCurrHP(), self.pokemon.getStat("HP")), None)
        self.healthEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        
    def draw(self):
        """ Draw the Pokemon Stats View """
        surface = GetTransparentSurface(self.width, self.height)
        
        pkmnSurface = self.pkmnEntryView.draw()
        surface.blit(pkmnSurface, (0,0))
        
        levelSurface = self.levelEntryView.draw()
        levelSurfacePosition = levelSurface.get_rect(right=self.width, top=0)
        surface.blit(levelSurface, levelSurfacePosition)
        
        healthBarSurface = self.healthBarView.draw()
        healthBarSurfacePosition = healthBarSurface.get_rect(top=pkmnSurface.get_height()+10, left=0)
        surface.blit(healthBarSurface, healthBarSurfacePosition)
        
        healthSurface = self.healthEntryView.draw()
        healthSurfacePosition = healthSurface.get_rect(top=pkmnSurface.get_height()+healthBarSurface.get_height()+15, right=self.width)
        surface.blit(healthSurface, healthSurfacePosition)
        
        return surface
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setLevelMenuEntryView()
        self.setHealthMenuEntryView()