from Screen.Console.screen import Screen
from Screen.Console.Battle.player_side_view import PlayerSideView
from Screen.Console.Menu.ActionMenu.action_menu_view import ActionMenuView

from kao_gui.console.console_screen import ConsoleScreen

class ActionMenuScreen(ConsoleScreen):
    """ Action Menu screen """
    
    def __init__(self, menu, playerSide, oppSide):
        """ Set up the Action Menu Screen """
        self.menuView = ActionMenuView(menu)
        self.playerSideView = PlayerSideView(playerSide)
        self.oppSideView = PlayerSideView(oppSide)
        
    def draw(self):
        """ Draw the window """
        self.drawOpponentSide()
        self.drawPlayerSide()
        self.drawMenuBox()

    def drawOpponentSide(self):
        """ Draws the Player Side """
        opponentSideLines = self.oppSideView.draw()
        self.drawAtPosition(opponentSideLines, (0, 0))

    def drawPlayerSide(self):
        """ Draws the Player Side """
        playerSideLines = self.playerSideView.draw()
        self.drawAtPosition(playerSideLines, (0, self.height-4-len(playerSideLines)))

    def drawMenuBox(self):
        """ Draws the Action Menu Box """
        menuBox, menuPos = self.menuView.draw()
        self.drawAtPosition(menuBox, (0, self.height-4))