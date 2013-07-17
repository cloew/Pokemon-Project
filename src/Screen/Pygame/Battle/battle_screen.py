from Screen.GUI.screen import Screen
from Screen.GUI.MessageBox.message_box import MessageBox

class BattleScreen(Screen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.bottomView = None
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if self.hasBottomView():
            self.bottomView.update()
        
    def draw(self, window):
        """ Draw the window """
        window.clear()
        if self.hasBottomView():
            bottomSurface = self.bottomView.draw()
            bottomSurfacePosition = bottomSurface.get_rect(left=self.getBottomWidgetLeftCoordinate(window), centery=self.getBottomWidgetYCoordinate(window))
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