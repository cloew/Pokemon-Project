from Screen.Console.screen import Screen
from Screen.Console.Battle.action_menu_view import ActionMenuView

class ActionMenuScreen(Screen):
    """ Action Menu screen """
    
    def __init__(self, menu):
        """ Set up the Action Menu Screen """
        self.menuView = ActionMenuView(menu)
        
    def draw(self, window):
        """ Draw the window """
        menuBox, menuPos = self.menuView.draw(window)
        window.draw(menuBox, (0,window.terminal.height-5))