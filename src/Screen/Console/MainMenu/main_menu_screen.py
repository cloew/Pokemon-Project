import blessings

from Screen.Console.screen import Screen
from logo import Logo
from menu_view import MenuView

class MainMenuScreen(Screen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def draw(self, window):
        """ Draws the screen to the provided window """
        self.drawLogo(window)
        self.drawMenu(window)
        
    def drawLogo(self, window):
        """ Draws the Logo to the window """
        logoText = self.logo.draw(window)
        logoPos = self.getCenteredRect(window, logoText, .5, .25) 
        window.draw(logoText, logoPos)
        
    def drawMenu(self, window):
        """ Draws the Menu to the window """
        menuSurf = self.menuView.draw(window)
        menuPos = self.getCenteredRect(window, menuSurf, .5, 11.0/16) 
        window.draw(menuSurf, menuPos)
        