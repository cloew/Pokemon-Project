from Menu.text_menu_entry import TextMenuEntry
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.HealthBar.health_bar_view import HealthBarView
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.label import Label
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class PokemonStatsView(SizedWidget):
    """ View for a Pokemon's Stats in a Battle """
    FONT_SIZE = 24
    
    def __init__(self, width, height, pokemon=None, pokemonMenuEntry=None, showHP=True):
        """ Initialize the Pokemon Stats View """
        SizedWidget.__init__(self, width, height)
        if pokemon is not None:
            self.pokemon = pokemon
        else:
            self.pokemon = pokemonMenuEntry.getPokemon()
            
        self.showHP = showHP
        self.setPokemonMenuEntryView(pokemonMenuEntry)
        self.setLevelLabel()
        self.setHealthLabel()
        self.healthBarView = HealthBarView(self.pokemon, width, height*.1)
    
    def setPokemonMenuEntryView(self, pokemonMenuEntry):
        """ Sets the Pokemon Menu Entry """
        if pokemonMenuEntry is None:
            pokemonMenuEntry = PokemonMenuEntry(self.pokemon, None)
        self.pkmnEntryView = MenuEntryView(pokemonMenuEntry, self.FONT_SIZE)
        
    def setLevelLabel(self):
        """ Set the Level Label """
        self.levelLabel = Label("Lv. {0}".format(self.pokemon.getLevel()), size=self.FONT_SIZE)
        
    def setHealthLabel(self):
        """ Set the Health Label """
        hpString = "{0}/{1}".format(self.pokemon.getCurrHP(), self.pokemon.getStat("HP"))
        self.healthLabel = Label(hpString, size=self.FONT_SIZE)
        
    def drawSurface(self):
        """ Draw the Pokemon Stats View """
        pkmnSurface = self.pkmnEntryView.draw()
        self.drawOnSurface(pkmnSurface, left=0, top=0)
        
        levelSurface = self.levelLabel.draw()
        self.drawOnSurface(levelSurface, right=1, top=0)
        
        healthBarSurface = self.healthBarView.draw()
        self.drawOnSurface(healthBarSurface, left=0, top=(pkmnSurface.get_height()+10.0)/self.height)
        
        if self.showHP:
            healthSurface = self.healthLabel.draw()
            self.drawOnSurface(healthSurface, right=1, 
                    top=(pkmnSurface.get_height()+healthBarSurface.get_height()+15.0)/self.height)
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setLevelLabel()
        self.setHealthLabel()