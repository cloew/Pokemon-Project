from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class OpponentSideView(BattleSideView):
    """ View for the opponent's side in a Pokemon Battle """
        
    def draw(self):
        """ Draw the Opponent Side View Surface and return it """
        surface = self.getBackgroundSurface()
        statsSurface = self.pokemonStatsView.draw()
        surface.blit(statsSurface, (self.width*.05,self.height*.1))
        
        surface.blit(self.pokemonImage, (self.width*.55, self.height*.05))
        
        return surface
        
    def shouldShowHP(self):
        """ Return if the Battle View should show the HP """
        return False