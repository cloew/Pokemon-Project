from logo import Logo
from Screen.Console.Menu.menu_view import MenuView

from kao_gui.console.console_widget import ConsoleWidget
from kao_gui.console.window import Window

class MainMenuScreen(ConsoleWidget):
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
        logoPos = self.getCenteredRect(logoSize, .5, .25) 
        self.drawAtPosition(logoText, logoPos)
        
    def drawMenu(self):
        """ Draws the Menu to the window """
        menuText, menuSize= self.menuView.draw()
        menuPos = self.getCenteredRect(menuSize, .5, 11.0/16) 
        self.drawAtPosition(menuText, menuPos)
        
    def getCenteredRect(self, size, xRatio, yRatio):
        """ Returns a position in that centers the text on the given percentage of the screen """
        width = Window.width
        height = Window.height
        
        centerWidth = xRatio*width
        centerHeight = yRatio*height
        centerWidth -= size[0]/2
        centerHeight -= size[1]/2
        return centerWidth, centerHeight
        
    def drawAtPosition(self, text, pos):
        """ Draws the text to the window """
        lineNum = pos[1]
        for line in text:
            with Window.terminal.location(int(pos[0]), int(lineNum)):
                print line
            lineNum += 1