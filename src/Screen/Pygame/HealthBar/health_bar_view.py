from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class HealthBarView(SizedWidget):
    """ View for a Pokemon's Health Bar """
    
    def __init__(self, pokemon, width, height):
        """  Initialize the Health Bar View """
        SizedWidget.__init__(self, width, height)
        self.pokemon = pokemon
        
    def drawSurface(self):
        """ Draw the Health Bar View and return its surface """
        healthBarSurface = GetTransparentSurface(self.width*self.getHealthPercentage()/100, self.height)
        healthBarSurface.fill(self.getHealthBarColor())
        self.drawOnSurface(healthBarSurface, left=0, top=0)
        
    def getHealthBarColor(self):
        """ Returns the Health Bar's color """
        healthPercentage = self.getHealthPercentage()
        colors = [(0, 255, 0),
                  (255, 255, 0),
                  (255, 0, 0)]

        color = ""
        if healthPercentage > 50:
            color = colors[0]
        elif healthPercentage > 10:
            color = colors[1]
        else:
            color = colors[2]
        return color
        
    def getHealthPercentage(self):
        """ Returns the percentage of the Pokemon's health """
        return (self.pokemon.getCurrHP()*100)/self.pokemon.getStat("HP")