from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

class BattleSideView:
    """ View for a battle side in a Pokemon Battle """
    
    def __init__(self, side):
        """ Initialize the Battle Side View """
        self.side = side
        menuEntry = PokemonMenuEntry(self.side.pkmnInPlay[0].pkmn, None)
        self.menuEntryView = MenuEntryView(menuEntry, None)
        
    def setSize(self, height, width):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
    def getBackgroundSurface(self):
        """ Returns the Background surface """
        surface = GetTransparentSurface(self.width, self.height)
        entrySurface = self.menuEntryView.draw()
        surface.blit(entrySurface, (0,0))
        return surface