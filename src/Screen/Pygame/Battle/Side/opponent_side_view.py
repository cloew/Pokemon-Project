from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class OpponentSideView(BattleSideView):
    """ View for the opponent's side in a Pokemon Battle """
        
    def drawSurface(self):
        """ Draw the Opponent Side View Surface and return it """
        statsSurface = self.pokemonStatsView.draw()
        self.drawOnSurface(statsSurface, left=.05, top=.1)
        self.drawOnSurface(self.pokemonImage, left=.55, top=.05)
        
    def shouldShowHP(self):
        """ Return if the Battle View should show the HP """
        return False