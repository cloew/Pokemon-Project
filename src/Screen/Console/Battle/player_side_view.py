from Screen.Console.view import View
from Screen.Console.Battle.player_pokemon_detail_view import PlayerPokemonDetailView

class PlayerSideView:
    """ Represents the view of the Player's Side in a battle """

    def __init__(self, side):
        """ Builds the Player Side View """
        self.side = side
        self.detailView = PlayerPokemonDetailView(side.pkmnInPlay[0])

    def draw(self, window):
        """ Returns the health bar as a console line """
        return self.detailView.draw(window)


    def getLines(self, window, width, height):
        """ """


    def getViewWidth(self, window):
        """ Returns the view width """
        return window.terminal.width

    def getViewHeight(self, window):
        """ Returns the view width """
        return (window.terminal.height - 4)/2