from Screen.Pygame.Menu.menu_with_background_widget import MenuWithBackgroundWidget

class MainMenuWidget(MenuWithBackgroundWidget):
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        MenuWithBackgroundWidget.__init__(self, menu, 220, 200)