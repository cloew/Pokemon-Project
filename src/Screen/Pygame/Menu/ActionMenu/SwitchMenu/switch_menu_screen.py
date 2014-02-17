from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView
from Screen.Pygame.Menu.two_column_menu_view import TwoColumnMenuView

from kao_gui.pygame.pygame_screen import PygameScreen

class SwitchMenuScreen(PygameScreen):
    """ View for the Switch Menu Screen """
    
    def __init__(self, menu):
        """ Builds the Switch Menu with all Pokemon """
        self.menu = menu
        self.menuView = TwoColumnMenuView(menu)
        
        self.statViews = []
        for entry in menu.entries:
            self.statViews.append(PokemonStatsView(pokemonMenuEntry=entry))
        self.menuView.entries = self.statViews
        
    def drawSurface(self):
        """ Draw the window """
        self.menuView.setSize(self.width, self.height)
        bottomSurface = self.menuView.draw()
        self.drawOnSurface(bottomSurface, left=0, top=0)