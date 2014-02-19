from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView
from Screen.Pygame.Menu.two_column_menu_view import TwoColumnMenuView

from kao_gui.pygame.pygame_screen import PygameScreen

class SwitchMenuScreen(PygameScreen):
    """ View for the Switch Menu Screen """
    
    def __init__(self, menu):
        """ Builds the Switch Menu with all Pokemon """
        PygameScreen.__init__(self)
        self.menu = menu
        self.menuView = TwoColumnMenuView(menu, self.width, self.height)
        
        self.statViews = []
        for entry in menu.entries:
            statView = PokemonStatsView(self.width*.9/self.menu.columns, self.height*.9/self.menu.columns,
                                        pokemonMenuEntry=entry)
            self.statViews.append(statView)
        self.menuView.entries = self.statViews
        
    def drawSurface(self):
        """ Draw the window """
        # self.menuView.setSize(self.width, self.height)
        bottomSurface = self.menuView.draw()
        self.drawOnSurface(bottomSurface, left=0, top=0)