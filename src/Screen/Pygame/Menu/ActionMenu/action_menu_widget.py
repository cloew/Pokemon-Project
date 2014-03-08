from Screen.Pygame.Menu.menu_widget import MenuWidget
from Screen.Pygame.Menu.menu_with_background_widget import MenuWithBackgroundWidget

class ActionMenuWidget(MenuWithBackgroundWidget):
    """ Represents the widget for the Action Menus """
    
    @property
    def columns(self):
        return 2.0
        
    @property
    def rows(self):
        return 2.0