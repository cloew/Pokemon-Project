from Screen.Console.Battle.player_side_view import PlayerSideView

from kao_gui.console.console_screen import ConsoleScreen

class BattleScreen(ConsoleScreen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.battle = battle
        self.playerSideView = PlayerSideView(battle.playerSide)
        self.oppSideView = PlayerSideView(battle.oppSide)
        
    def draw(self):
        """ Draw the window """
        self.drawOpponentSide()
        self.drawPlayerSide()
        self.drawBottomWidget()

    def drawOpponentSide(self):
        """ Draws the Player Side """
        opponentSideLines = self.oppSideView.draw()
        self.drawAtPosition(opponentSideLines, (0, 0))

    def drawPlayerSide(self):
        """ Draws the Player Side """
        playerSideLines = self.playerSideView.draw()
        self.drawAtPosition(playerSideLines, (0, self.height-4-len(playerSideLines)))
        
    def drawBottomWidget(self):
        """ Draws the Message Box """
        bottomLines = self.getBottomLines()
        self.drawAtPosition(bottomLines, (0, self.height-4))

    def getBottomLines(self):
        """ Draws the Message Box.
            Override in sub class """