from Screen.Pygame.screen import Screen
from Screen.Pygame.Menu.two_column_menu_view import TwoColumnMenuView

class SwitchMenuScreen(Screen):
    """ View for the Switch Menu Screen """
    
     def __init__(self, menu):
        """ Builds the Battle View with the Battle """
        self.menuView = TwoColumnMenuView(menu)
        
    def update(self):
        """ Update the screen """
        self.menuView.update()
        
    def draw(self, window):
        """ Draw the window """
        window.clear()
        
        self.menuView.setSize(window.width, window.height)
        bottomSurface = self.menuView.draw()
        window.draw(bottomSurface, (0,0))