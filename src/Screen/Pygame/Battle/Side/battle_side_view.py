from Screen.Pygame.pygame_helper import GetTransparentSurface, load_image
from Screen.Pygame.Battle.Side.pokemon_stats_view import PokemonStatsView

class BattleSideView:
    """ View for a battle side in a Pokemon Battle """
    
    def __init__(self, side):
        """ Initialize the Battle Side View """
        self.side = side
        self.pokemonStatsView = PokemonStatsView(self.side.pkmnInPlay[0])
        self.setPokemonImage()
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.height = height
        self.width = width
        
    def update(self):
        """ Update the Battle Side View """
        self.pokemonStatsView.update()
        self.setPokemonImage()
        
    def getBackgroundSurface(self):
        """ Returns the Background surface """
        surface = GetTransparentSurface(self.width, self.height)
        return surface
        
    def setPokemonImage(self):
        """ Set the pokemon Image """
        self.pokemonImage = load_image("{0}.png".format(self.getBasePokemonImageName()))
        
    def getBasePokemonImageName(self):
        """ Returns the base Pokemon Image Name """
        return "Pokemon/{0}".format(self.getPokemon().species.lower())
        
    def getPokemon(self):
        """ Returns the current Pokemon object """
        return self.side.pkmnInPlay[0].pkmn