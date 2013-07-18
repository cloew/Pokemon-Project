from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class PlayerSideView(BattleSideView):
    """ View for the player's side in a Pokemon Battle """
        
    def draw(self):
        """ Draw the Player Side View Surface and return it """
        surface = self.getBackgroundSurface()
        
        entrySurface = self.menuEntryView.draw()
        surface.blit(entrySurface, (self.width*.55,self.height*.1))
        
        surface.blit(self.pokemonImage, (self.width*.05, self.height*.05))
        
        return surface
        
    def getBasePokemonImageName(self):
        """ Returns the base Pokemon Image Name """
        return "{0}_back".format(BattleSideView.getBasePokemonImageName(self))