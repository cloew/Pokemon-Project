from logo import Logo
from Screen.Console.Menu.menu_view import MenuView

from kao_gui.console.console_screen import ConsoleScreen

class MainMenuScreen(ConsoleScreen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def draw(self):
        """ Draws the screen """
        self.drawLogo()
        self.drawMenu()
        
    def drawLogo(self):
        """ Draws the Logo to the window """
        logoText, logoSize = self.logo.draw()
        self.drawCenteredText(logoText, logoSize, .5, .25)
        
    def drawMenu(self):
        """ Draws the Menu to the window """
        menuText, menuSize = self.menuView.draw() 
        self.drawCenteredText(menuText, menuSize, .5, 11.0/16)