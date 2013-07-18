from Screen.Pygame.pygame_helper import GetTransparentSurface

class HealthBarView:
    """ View for a Pokemon's Health Bar """
    
    def __init__(self, pokemon):
        """  Initialize the Health Bar View """
        self.pokemon = pokemon
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
    def draw(self):
        """ Draw the Health Bar View and return its surface """
        surface = GetTransparentSurface(self.width, self.height)
        healthBarSurface = GetTransparentSurface(self.width*self.getHealthPercentage()/100, self.height)
        healthBarSurface.fill(self.getHealthBarColor())
        surface.blit(healthBarSurface, (0,0))
        return surface
        
    def update(self):
        """ Do nothing """
        
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