from Screen.Pygame.Battle.Side.battle_side_view import BattleSideView

class PlayerSideView(BattleSideView):
    """ View for the player's side in a Pokemon Battle """
        
    def draw(self):
        """ Draw the Player Side View Surface and return it """
        return self.getBackgroundSurface()
    
    def update(self):
        """ Update the Player Side """