from Menu.text_menu_entry import TextMenuEntry
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.HealthBar.health_bar_view import HealthBarView
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonStatsView:
    """ View for a Pokemon's Stats in a Battle """
    FONT_SIZE = 24
    
    def __init__(self, pokemon):
        """ Initialize the Pokemon Stats View """
        self.pokemon = pokemon
        self.setPokemonMenuEntryView()
        self.healthBarView = HealthBarView(self.pokemon)
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
        self.healthBarView.setSize(self.width, self.height*.1)
    
    def setPokemonMenuEntryView(self):
        """ Sets the Pokemon Menu Entry """
        menuEntry = PokemonMenuEntry(self.getPokemon(), None)
        self.pkmnEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        self.setLevelMenuEntryView()
        
    def setLevelMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("Lv. {0}".format(self.pokemon.getLevel()), None)
        self.levelEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        
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
        
        return surface
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setPokemonMenuEntryView()
        
    def getPokemon(self):
        """ Return the pokemon """
        return self.pokemon.pkmn