from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class PlayerSideView(BattleSideView):
    """ View for the player's side in a Pokemon Battle """
        
    def drawSurface(self):
        """ Draw the Player Side View Surface and return it """
        statsSurface = self.pokemonStatsView.draw()
        self.drawOnSurface(statsSurface, left=.55, top=.1)
        self.drawOnSurface(self.pokemonImage, left=.05, top=.05)
        
    def getBasePokemonImageName(self):
        """ Returns the base Pokemon Image Name """
        return "{0}_back".format(BattleSideView.getBasePokemonImageName(self))