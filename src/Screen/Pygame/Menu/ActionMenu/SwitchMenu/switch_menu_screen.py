from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_widget import SwitchMenuWidget

from kao_gui.pygame.pygame_screen import PygameScreen

class SwitchMenuScreen(PygameScreen):
    """ View for the Switch Menu Screen """
    
    def __init__(self, menu):
        """ Builds the Switch Menu with all Pokemon """
        PygameScreen.__init__(self)
        self.menu = menu
        self.menuView = SwitchMenuWidget(menu, self.width, self.height)
        
        self.statViews = []
        width = self.width*.9/self.menu.columns
        height = self.height*.9/self.menu.columns
        for entry in menu.entries:
            statView = PokemonStatsView(width, height,
                                        pokemonMenuEntry=entry)
            self.statViews.append(statView)
        self.menuView.entries = self.statViews
        
    def drawSurface(self):
        """ Draw the window """
        bottomSurface = self.menuView.draw()
        self.drawOnSurface(bottomSurface, left=0, top=0)