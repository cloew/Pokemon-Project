from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView

from kao_gui.pygame.pygame_helper import GetTransparentSurface, load_image
from kao_gui.pygame.pygame_widget import PygameWidget

class BattleSideView(PygameWidget):
    """ View for a battle side in a Pokemon Battle """
    
    def __init__(self, side):
        """ Initialize the Battle Side View """
        self.side = side
        self.pokemonStatsView = PokemonStatsView(self.side.pkmnInPlay[0], showHP=self.shouldShowHP())
        self.setPokemonImage()
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.__height = height
        self.__width = width
        
        self.pokemonStatsView.setSize(self.__width*.4, self.__height*.9)
        
    def buildSurface(self):
        """ Return the surface for the widget """
        return GetTransparentSurface(self.__width, self.__height)
        
    def update(self):
        """ Update the Battle Side View """
        self.setPokemonImage()
        
    def setPokemonImage(self):
        """ Set the pokemon Image """
        self.pokemonImage = load_image("{0}.png".format(self.getBasePokemonImageName()))
        
    def getBasePokemonImageName(self):
        """ Returns the base Pokemon Image Name """
        return "resources/images/Pokemon/{0}".format(self.getPokemon().getDisplayImageBaseName())
        
    def getPokemon(self):
        """ Returns the current Pokemon object """
        return self.side.pkmnInPlay[0].pkmn
        
    def shouldShowHP(self):
        """ Return if the Battle View should show the HP """
        return True 