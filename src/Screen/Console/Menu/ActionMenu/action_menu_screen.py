from Screen.Console.Battle.battle_screen import BattleScreen
from Screen.Console.Menu.ActionMenu.action_menu_view import ActionMenuView

class ActionMenuScreen(BattleScreen):
    """ Action Menu screen """
    
    def __init__(self, menu, battle):
        """ Set up the Action Menu Screen """
        self.menuView = ActionMenuView(menu)
        BattleScreen.__init__(self, battle)
        
    def getBottomLines(self):
        """ Returns the Message Box """
        menuBox, menuSize = self.menuView.draw()
        return menuBox