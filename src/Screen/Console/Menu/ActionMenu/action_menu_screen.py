from Screen.Console.screen import Screen
from Screen.Console.Battle.action_menu_view import ActionMenuView
from Screen.Console.Battle.player_side_view import PlayerSideView

class ActionMenuScreen(Screen):
    """ Action Menu screen """
    
    def __init__(self, menu, playerSide, oppSide):
        """ Set up the Action Menu Screen """
        self.menuView = ActionMenuView(menu)
        self.playerSideView = PlayerSideView(playerSide)
        self.oppSideView = PlayerSideView(oppSide)
        
    def draw(self, window):
        """ Draw the window """
        self.drawOpponentSide(window)
        self.drawPlayerSide(window)
        self.drawMenuBox(window)

    def drawOpponentSide(self, window):
        """ Draws the Player Side """
        opponentSideLines = self.oppSideView.draw(window)
        window.draw(opponentSideLines, (0, 0))

    def drawPlayerSide(self, window):
        """ Draws the Player Side """
        playerSideLines = self.playerSideView.draw(window)
        window.draw(playerSideLines, (0, window.terminal.height-5-len(playerSideLines)))

    def drawMenuBox(self, window):
        """ Draws the Action Menu Box """
        menuBox, menuPos = self.menuView.draw(window)
        window.draw(menuBox, (0,window.terminal.height-5))