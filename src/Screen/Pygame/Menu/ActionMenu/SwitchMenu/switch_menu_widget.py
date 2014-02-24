from Screen.Pygame.Menu.menu_widget import MenuWidget

class SwitchMenuWidget(MenuWidget):
    """ Represents the widget for the Swicth Menu """
    
    @property
    def columns(self):
        return 2.0
        
    @property
    def rows(self):
        return 3.0