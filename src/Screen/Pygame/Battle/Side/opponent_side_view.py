from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class OpponentSideView(BattleSideView):
    """ View for the opponent's side in a Pokemon Battle """
        
    def draw(self):
        """ Draw the Opponent Side View Surface and return it """
        surface = self.getBackgroundSurface()
        entrySurface = self.menuEntryView.draw()
        surface.blit(entrySurface, (self.width*.05,self.height*.1))
        return surface