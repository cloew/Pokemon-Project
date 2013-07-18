from Screen.Pygame.screen import Screen
from Screen.Pygame.Battle.Side.opponent_side_view import OpponentSideView
from Screen.Pygame.Battle.Side.player_side_view import PlayerSideView

class BattleScreen(Screen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.opponentView = OpponentSideView(battle.oppSide)
        self.playerView = PlayerSideView(battle.playerSide)
        self.bottomView = None
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if self.hasBottomView():
            self.bottomView.update()
        
    def draw(self, window):
        """ Draw the window """
        window.clear()
        
        self.opponentView.setSize(window.width, window.height*.35)
        oppSideSurface = self.opponentView.draw()
        window.draw(oppSideSurface, (0, 0))
        
        self.playerView.setSize(window.width, window.height*.35)
        playerSideSurface = self.playerView.draw()
        window.draw(playerSideSurface, (0, window.height*.35))
        
        if self.hasBottomView():
            self.bottomView.setSize(window.width*.9, window.height*.3)
            bottomSurface = self.bottomView.draw()
            bottomSurfacePosition = bottomSurface.get_rect(left=window.width/20, top=window.height*.7)
            window.draw(bottomSurface, bottomSurfacePosition)
            
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