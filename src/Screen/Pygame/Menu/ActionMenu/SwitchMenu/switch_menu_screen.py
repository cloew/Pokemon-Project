from Screen.Pygame.screen import Screen
from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView
from Screen.Pygame.Menu.two_column_menu_view import TwoColumnMenuView

class SwitchMenuScreen(Screen):
    """ View for the Switch Menu Screen """
    
    def __init__(self, menu):
        """ Builds the Battle View with the Battle """
        self.menu = menu
        self.menuView = TwoColumnMenuView(menu)
        
        self.statViews = []
        for entry in menu.entries:
            self.statViews.append(PokemonStatsView(entry.getPokemon()))
        self.menuView.entries = self.statViews    
        
    def update(self):
        """ Update the screen """
        self.menuView.update()
        
        for entry, statView in zip(self.menu.entries, self.statViews):
            if entry.selected:
                statView.select()
            else:
                statView.deselect()
            
        
    def draw(self, window):
        """ Draw the window """
        window.clear()
        
        self.menuView.setSize(window.width, window.height)
        bottomSurface = self.menuView.draw()
        window.draw(bottomSurface, (0,0))