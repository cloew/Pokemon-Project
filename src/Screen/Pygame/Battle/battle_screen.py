from Screen.Pygame.Battle.Side.opponent_side_view import OpponentSideView
from Screen.Pygame.Battle.Side.player_side_view import PlayerSideView

from kao_gui.pygame.pygame_screen import PygameScreen

class BattleScreen(PygameScreen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.opponentView = OpponentSideView(battle.oppSide)
        self.playerView = PlayerSideView(battle.playerSide)
        self.bottomView = None
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        self.opponentView.update()
        self.playerView.update()
        if self.hasBottomView():
            self.bottomView.update()
        
    def drawSurface(self):
        """ Draw the window """
        self.opponentView.setSize(self.width, self.height*.35)
        oppSideSurface = self.opponentView.draw()
        self.drawOnSurface(oppSideSurface, left=0, top=0)
        
        self.playerView.setSize(self.width, self.height*.35)
        playerSideSurface = self.playerView.draw()
        self.drawOnSurface(playerSideSurface, left=0, top=.35)
        
        if self.hasBottomView():
            self.bottomView.setSize(self.width*.9, self.height*.3)
            bottomSurface = self.bottomView.draw()
            self.drawOnSurface(bottomSurface, left=.05, top=.7)
            
    def setBottomView(self, view):
        """ Set the Bottom View """
        self.bottomView = view
        
    def hasBottomView(self):
        """ Return if the Screen has a Botton View """
        return self.bottomView is not None
        
    def getBottomWidgetLeftCoordinate(self, window):
        """  """
        return window.width/20
        
    def getBottomWidgetYCoordinate(self, window):
        """  """
        return 3*window.height/4