from Screen.Pygame.Menu.menu_widget import MenuWidget

class ActionMenuWidget(MenuWidget):
    """ Represents the widget for the Action Menus """
    
    @property
    def columns(self):
        return 2.0
        
    @property
    def rows(self):
        return 2.0