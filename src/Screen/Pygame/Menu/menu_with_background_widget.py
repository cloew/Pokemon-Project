from Screen.Pygame.Menu.menu_widget import MenuWidget
from Screen.Pygame.Menu.menu_background_widget import MenuBackgroundWidget
from Screen.Pygame.Menu.menu_entry_widget import MenuEntryWidget

from kao_gui.pygame.pygame_widget import PygameWidget

class MenuWithBackgroundWidget(MenuWidget):
    """ Represents the widget for a Menu With A Background """
    
    def __init__(self, menu, width, height, MenuEntryWidget=MenuEntryWidget):
        """ Initialize the widget """
        MenuWidget.__init__(self, menu, width, height, MenuEntryWidget=MenuEntryWidget)
        self.background = MenuBackgroundWidget(width, height)
        
    def buildSurface(self):
        """ Build the Men Surface """
        return self.background.draw()